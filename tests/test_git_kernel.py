from unittest import TestCase
from src.git_kernel.git_kernel import GitKernel


class TestKernel(TestCase):
    def test_porcess_code(self):
        input_code = "this is some code"

        git_kernel = GitKernel()

        new_repo, code = git_kernel.process_code(input_code)
        self.assertFalse(new_repo)
        self.assertEqual(input_code, code)

        new_repo, code = git_kernel.process_code(
            "%init\n" + code
        )
        self.assertTrue(new_repo)
        self.assertEqual(input_code, code)
