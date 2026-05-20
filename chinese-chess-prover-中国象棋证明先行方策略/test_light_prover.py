import unittest

from light_prover import Board, DfpnProver, Prover, START_FEN, threshold_report, verify_proof


class LightProverTest(unittest.TestCase):
    def test_start_position_has_44_legal_moves(self):
        board = Board.from_fen(START_FEN)
        self.assertEqual(len(board.legal_moves()), 44)

    def test_terminal_no_legal_moves_is_loss(self):
        board = Board.from_fen("3RkR3/3RRR3/9/9/9/9/9/9/9/4K4 b - - 0 1")
        self.assertEqual(len(board.legal_moves()), 0)
        result = Prover().prove(board, 0)
        self.assertEqual(result.status, "LOSS")
        verify_proof(result.proof)

    def test_bounded_win_certificate_verifies(self):
        board = Board.from_fen("3RkR3/3R1R3/4R4/9/9/9/9/9/9/4K4 w - - 0 1")
        result = Prover().prove(board, 1)
        self.assertEqual(result.status, "WIN")
        verify_proof(result.proof)

    def test_dfpn_win_certificate_verifies(self):
        board = Board.from_fen("3RkR3/3R1R3/4R4/9/9/9/9/9/9/4K4 w - - 0 1")
        result = DfpnProver(max_nodes=100).prove(board, 1)
        self.assertEqual(result.status, "WIN")
        self.assertEqual(result.pn, 0)
        verify_proof(result.proof)

    def test_threshold_report_is_sample_bounded(self):
        report = threshold_report(
            [
                {"score_scalar": 1200, "status": "WIN"},
                {"score_scalar": 900, "status": "WIN"},
                {"score_scalar": 800, "status": "UNKNOWN"},
            ]
        )
        self.assertEqual(report["threshold_all_above_proven_win"], 900)
        self.assertIn("not a theorem", report["warning"])


if __name__ == "__main__":
    unittest.main()
