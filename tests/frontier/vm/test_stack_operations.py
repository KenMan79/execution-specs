from functools import partial

import pytest

from tests.frontier.vm.vm_test_helpers import run_test

run_push_vm_test = partial(
    run_test,
    "tests/fixtures/LegacyTests/Constantinople/VMTests/vmPushDupSwapTest",
)
run_pop_vm_test = partial(
    run_test,
    "tests/fixtures/LegacyTests/Constantinople/VMTests/vmIOandFlowOperations",
)
run_dup_vm_test = run_swap_vm_test = run_push_vm_test


@pytest.mark.parametrize(
    "test_file",
    [f"push{i}.json" for i in range(1, 34)]
    + [
        "push32Undefined2.json",
        "push32AndSuicide.json",
    ],
)
def test_push_successfully(test_file: str) -> None:
    run_push_vm_test(test_file)


@pytest.mark.parametrize(
    "test_file",
    [
        "push1_missingStack.json",
        "push32Undefined.json",
        "push32Undefined3.json",
        "push32FillUpInputWithZerosAtTheEnd.json",
    ],
)
def test_push_failed(test_file: str) -> None:
    run_push_vm_test(test_file)


def test_dup() -> None:
    for i in range(1, 17):
        run_dup_vm_test(f"dup{i}.json")


def test_dup_error() -> None:
    run_dup_vm_test("dup2error.json")


def test_swap() -> None:
    for i in range(1, 17):
        run_swap_vm_test(f"swap{i}.json")


def test_swap_jump() -> None:
    run_swap_vm_test("swapjump1.json")


def test_swap_error() -> None:
    run_swap_vm_test("swap2error.json")


def test_pop() -> None:
    run_pop_vm_test("pop0.json")


def test_pop_fails_when_stack_underflowed() -> None:
    run_pop_vm_test("pop1.json")
