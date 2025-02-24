import os
from functools import partial

import pytest

from tests.frontier.blockchain_st_test_helpers import (
    run_frontier_blockchain_st_tests,
)

run_example_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stExample/",
)

run_transaction_init_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stTransactionTest/",
)

run_log_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stLogTests/",
)

run_precompiles_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stPreCompiledContracts2/",
)

run_system_operations_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stSystemOperationsTest/",
)

run_create_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stCreateTest/",
)

run_uncles_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests",
)

run_transaction_test = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stTransactionTest/",
)

run_random2_tests = partial(
    run_frontier_blockchain_st_tests,
    "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
    "GeneralStateTests/stRandom2/",
)


def test_add() -> None:
    run_example_test("add11_d0g0v0.json")


@pytest.mark.parametrize(
    "test_file",
    [
        f"Opcodes_TransactionInit_d{i}g0v0.json"
        for i in range(128)
        if i not in [33, 127]
        # NOTE:
        # - Test 33, 127 has no tests for Frontier
    ],
)
def test_transaction_init(test_file: str) -> None:
    run_transaction_init_test(test_file)


@pytest.mark.parametrize(
    "test_file",
    [
        "log0_emptyMem_d0g0v0.json",
        "log0_logMemsizeZero_d0g0v0.json",
        "log0_nonEmptyMem_d0g0v0.json",
        "log0_nonEmptyMem_logMemSize1_d0g0v0.json",
        "log0_nonEmptyMem_logMemSize1_logMemStart31_d0g0v0.json",
        "log1_Caller_d0g0v0.json",
        "log1_MaxTopic_d0g0v0.json",
        "log1_emptyMem_d0g0v0.json",
        "log1_logMemsizeZero_d0g0v0.json",
        "log1_nonEmptyMem_d0g0v0.json",
        "log1_nonEmptyMem_logMemSize1_d0g0v0.json",
        "log1_nonEmptyMem_logMemSize1_logMemStart31_d0g0v0.json",
        "log2_Caller_d0g0v0.json",
        "log2_MaxTopic_d0g0v0.json",
        "log2_emptyMem_d0g0v0.json",
        "log2_logMemsizeZero_d0g0v0.json",
        "log2_nonEmptyMem_d0g0v0.json",
        "log2_nonEmptyMem_logMemSize1_d0g0v0.json",
        "log2_nonEmptyMem_logMemSize1_logMemStart31_d0g0v0.json",
        "log3_Caller_d0g0v0.json",
        "log3_MaxTopic_d0g0v0.json",
        "log3_PC_d0g0v0.json",
        "log3_emptyMem_d0g0v0.json",
        "log3_logMemsizeZero_d0g0v0.json",
        "log3_nonEmptyMem_d0g0v0.json",
        "log3_nonEmptyMem_logMemSize1_d0g0v0.json",
        "log3_nonEmptyMem_logMemSize1_logMemStart31_d0g0v0.json",
        "log4_Caller_d0g0v0.json",
        "log4_MaxTopic_d0g0v0.json",
        "log4_PC_d0g0v0.json",
        "log4_emptyMem_d0g0v0.json",
        "log4_logMemsizeZero_d0g0v0.json",
        "log4_nonEmptyMem_d0g0v0.json",
        "log4_nonEmptyMem_logMemSize1_d0g0v0.json",
        "log4_nonEmptyMem_logMemSize1_logMemStart31_d0g0v0.json",
        "log0_logMemStartTooHigh_d0g0v0.json",
        "log0_logMemsizeTooHigh_d0g0v0.json",
        "log1_logMemStartTooHigh_d0g0v0.json",
        "log1_logMemsizeTooHigh_d0g0v0.json",
        "log2_logMemStartTooHigh_d0g0v0.json",
        "log2_logMemsizeTooHigh_d0g0v0.json",
        "log3_logMemStartTooHigh_d0g0v0.json",
        "log3_logMemsizeTooHigh_d0g0v0.json",
        "log4_logMemStartTooHigh_d0g0v0.json",
        "log4_logMemsizeTooHigh_d0g0v0.json",
        "logInOOG_Call_d0g0v0.json",
    ],
)
def test_log_operations(test_file: str) -> None:
    run_log_test(test_file)


@pytest.mark.parametrize(
    "test_file",
    [
        "CALLCODEEcrecover0_0input_d0g0v0.json",
        "CALLCODEEcrecover0_0input_d0g0v0.json",
        "CALLCODEEcrecover0_Gas2999_d0g0v0.json",
        "CALLCODEEcrecover0_NoGas_d0g0v0.json",
        "CALLCODEEcrecover0_completeReturnValue_d0g0v0.json",
        "CALLCODEEcrecover0_d0g0v0.json",
        "CALLCODEEcrecover0_gas3000_d0g0v0.json",
        "CALLCODEEcrecover0_overlappingInputOutput_d0g0v0.json",
        "CALLCODEEcrecover1_d0g0v0.json",
        "CALLCODEEcrecover2_d0g0v0.json",
        "CALLCODEEcrecover3_d0g0v0.json",
        "CALLCODEEcrecover80_d0g0v0.json",
        "CALLCODEEcrecoverH_prefixed0_d0g0v0.json",
        "CALLCODEEcrecoverR_prefixed0_d0g0v0.json",
        "CALLCODEEcrecoverS_prefixed0_d0g0v0.json",
        "CALLCODEEcrecoverV_prefixed0_d0g0v0.json",
        "CALLCODEEcrecoverV_prefixedf0_d0g0v0.json",
        "CALLCODEEcrecoverV_prefixedf0_d1g0v0.json",
        "CALLCODEIdentitiy_0_d0g0v0.json",
        "CALLCODEIdentitiy_1_d0g0v0.json",
        "CALLCODEIdentity_1_nonzeroValue_d0g0v0.json",
        "CALLCODEIdentity_2_d0g0v0.json",
        "CALLCODEIdentity_3_d0g0v0.json",
        "CALLCODEIdentity_4_d0g0v0.json",
        "CALLCODEIdentity_4_gas17_d0g0v0.json",
        "CALLCODEIdentity_4_gas18_d0g0v0.json",
        "CALLCODEIdentity_5_d0g0v0.json",
        "CALLCODERipemd160_0_d0g0v0.json",
        "CALLCODERipemd160_1_d0g0v0.json",
        "CALLCODERipemd160_2_d0g0v0.json",
        "CALLCODERipemd160_3_d0g0v0.json",
        "CALLCODERipemd160_3_postfixed0_d0g0v0.json",
        "CALLCODERipemd160_3_prefixed0_d0g0v0.json",
        "CALLCODERipemd160_4_d0g0v0.json",
        "CALLCODERipemd160_4_gas719_d0g0v0.json",
        "CALLCODERipemd160_5_d0g0v0.json",
        "CALLCODESha256_0_d0g0v0.json",
        "CALLCODESha256_1_d0g0v0.json",
        "CALLCODESha256_1_nonzeroValue_d0g0v0.json",
        "CALLCODESha256_2_d0g0v0.json",
        "CALLCODESha256_3_d0g0v0.json",
        "CALLCODESha256_3_postfix0_d0g0v0.json",
        "CALLCODESha256_3_prefix0_d0g0v0.json",
        "CALLCODESha256_4_d0g0v0.json",
        "CALLCODESha256_4_gas99_d0g0v0.json",
        "CALLCODESha256_5_d0g0v0.json",
        "CallEcrecover0_0input_d0g0v0.json",
        "CallEcrecover0_Gas2999_d0g0v0.json",
        "CallEcrecover0_NoGas_d0g0v0.json",
        "CallEcrecover0_completeReturnValue_d0g0v0.json",
        "CallEcrecover0_d0g0v0.json",
        "CallEcrecover0_gas3000_d0g0v0.json",
        "CallEcrecover0_overlappingInputOutput_d0g0v0.json",
        "CallEcrecover1_d0g0v0.json",
        "CallEcrecover2_d0g0v0.json",
        "CallEcrecover3_d0g0v0.json",
        "CallEcrecover80_d0g0v0.json",
        "CallEcrecoverCheckLengthWrongV_d0g0v0.json",
        "CallEcrecoverCheckLength_d0g0v0.json",
        "CallEcrecoverH_prefixed0_d0g0v0.json",
        "CallEcrecoverInvalidSignature_d0g0v0.json",
        "CallEcrecoverR_prefixed0_d0g0v0.json",
        "CallEcrecoverS_prefixed0_d0g0v0.json",
        "CallEcrecoverUnrecoverableKey_d0g0v0.json",
        "CallEcrecoverV_prefixed0_d0g0v0.json",
        "CallIdentitiy_0_d0g0v0.json",
        "CallIdentitiy_1_d0g0v0.json",
        "CallIdentity_1_nonzeroValue_d0g0v0.json",
        "CallIdentity_2_d0g0v0.json",
        "CallIdentity_3_d0g0v0.json",
        "CallIdentity_4_d0g0v0.json",
        "CallIdentity_4_gas17_d0g0v0.json",
        "CallIdentity_4_gas18_d0g0v0.json",
        "CallIdentity_5_d0g0v0.json",
        "CallIdentity_6_inputShorterThanOutput_d0g0v0.json",
        "CallRipemd160_0_d0g0v0.json",
        "CallRipemd160_1_d0g0v0.json",
        "CallRipemd160_2_d0g0v0.json",
        "CallRipemd160_3_d0g0v0.json",
        "CallRipemd160_3_postfixed0_d0g0v0.json",
        "CallRipemd160_3_prefixed0_d0g0v0.json",
        "CallRipemd160_4_d0g0v0.json",
        "CallRipemd160_4_gas719_d0g0v0.json",
        "CallRipemd160_5_d0g0v0.json",
        "CallSha256_0_d0g0v0.json",
        "CallSha256_1_d0g0v0.json",
        "CallSha256_1_nonzeroValue_d0g0v0.json",
        "CallSha256_2_d0g0v0.json",
        "CallSha256_3_d0g0v0.json",
        "CallSha256_3_postfix0_d0g0v0.json",
        "CallSha256_3_prefix0_d0g0v0.json",
        "CallSha256_4_d0g0v0.json",
        "CallSha256_4_gas99_d0g0v0.json",
        "CallSha256_5_d0g0v0.json",
    ],
)
def test_precompiles(test_file: str) -> None:
    run_precompiles_test(test_file)


@pytest.mark.parametrize(
    "test_file",
    [
        "ABAcalls0_d0g0v0.json",
        "ABAcalls1_d0g0v0.json",
        "ABAcalls2_d0g0v0.json",
        "ABAcalls3_d0g0v0.json",
        "ABAcallsSuicide0_d0g0v0.json",
        "ABAcallsSuicide1_d0g0v0.json",
        "suicideAddress_d0g0v0.json",
        "suicideCaller_d0g0v0.json",
        "suicideCallerAddresTooBigLeft_d0g0v0.json",
        "suicideCallerAddresTooBigRight_d0g0v0.json",
        "suicideNotExistingAccount_d0g0v0.json",
        "suicideOrigin_d0g0v0.json",
        "suicideSendEtherPostDeath_d0g0v0.json",
        "suicideSendEtherToMe_d0g0v0.json",
        "callerAccountBalance_d0g0v0.json",
        "CreateHashCollision_d0g0v0.json",
    ],
)
def test_system_operations(test_file: str) -> None:
    run_system_operations_test(test_file)


@pytest.mark.parametrize(
    "test_file",
    [
        "CREATE_AcreateB_BSuicide_BStore_d0g0v0.json",
        "CREATE_ContractRETURNBigOffset_d0g0v0.json",
        "CREATE_ContractRETURNBigOffset_d1g0v0.json",
        "CREATE_ContractRETURNBigOffset_d2g0v0.json",
        "CREATE_ContractRETURNBigOffset_d3g0v0.json",
        "CREATE_ContractSSTOREDuringInit_d0g0v0.json",
        "CREATE_ContractSuicideDuringInit_ThenStoreThenReturn_d0g0v0.json",
        "CREATE_ContractSuicideDuringInit_WithValueToItself_d0g0v0.json",
        "CREATE_ContractSuicideDuringInit_WithValue_d0g0v0.json",
        "CREATE_ContractSuicideDuringInit_d0g0v0.json",
        "CREATE_EContractCreateEContractInInit_Tr_d0g0v0.json",
        "CREATE_EContractCreateNEContractInInitOOG_Tr_d0g0v0.json",
        "CREATE_EContractCreateNEContractInInit_Tr_d0g0v0.json",
        "CREATE_EContract_ThenCALLToNonExistentAcc_d0g0v0.json",
        "CREATE_EmptyContractAndCallIt_0wei_d0g0v0.json",
        "CREATE_EmptyContractAndCallIt_1wei_d0g0v0.json",
        "CREATE_EmptyContractWithBalance_d0g0v0.json",
        "CREATE_EmptyContractWithStorageAndCallIt_0wei_d0g0v0.json",
        "CREATE_EmptyContractWithStorageAndCallIt_1wei_d0g0v0.json",
        "CREATE_EmptyContractWithStorage_d0g0v0.json",
        "CREATE_EmptyContract_d0g0v0.json",
        "CREATE_empty000CreateinInitCode_Transaction_d0g0v0.json",
        "CreateCollisionToEmpty_d0g0v0.json",
        "CreateCollisionToEmpty_d0g0v1.json",
        "TransactionCollisionToEmptyButCode_d0g0v0.json",
        "TransactionCollisionToEmptyButCode_d0g0v1.json",
        "TransactionCollisionToEmptyButNonce_d0g0v0.json",
        "TransactionCollisionToEmptyButNonce_d0g0v1.json",
        "TransactionCollisionToEmpty_d0g0v0.json",
        "TransactionCollisionToEmpty_d0g0v1.json",
        # Note: All other tests from stCreateTest that aren't listed
        # here don't have tests for Frontier.
    ],
)
def test_create(test_file: str) -> None:
    run_create_test(test_file)


@pytest.mark.parametrize(
    "test_file",
    [
        "ValidBlocks/bcUncleTest/oneUncle.json",
        "ValidBlocks/bcUncleTest/oneUncleGeneration2.json",
        "ValidBlocks/bcUncleTest/oneUncleGeneration3.json",
        "ValidBlocks/bcUncleTest/oneUncleGeneration4.json",
        "ValidBlocks/bcUncleTest/oneUncleGeneration5.json",
        "ValidBlocks/bcUncleTest/oneUncleGeneration6.json",
        "ValidBlocks/bcUncleTest/twoUncle.json",
        "ValidBlocks/bcUncleTest/uncleHeaderAtBlock2.json",
        "ValidBlocks/bcUncleSpecialTests/uncleBloomNot0.json",
        "ValidBlocks/bcUncleSpecialTests/futureUncleTimestampDifficultyDrop.json",
        "InvalidBlocks/bcUncleHeaderValidity/correct.json",
    ],
)
def test_uncles_correctness(test_file: str) -> None:
    run_uncles_test(test_file)


def test_invalid_uncles() -> None:
    invalid_blocks_dir = (
        "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
        "InvalidBlocks"
    )

    for test_file in os.listdir(f"{invalid_blocks_dir}/bcUncleTest"):
        with pytest.raises(AssertionError):
            run_uncles_test(f"InvalidBlocks/bcUncleTest/{test_file}")

    for test_file in os.listdir(f"{invalid_blocks_dir}/bcUncleHeaderValidity"):
        if test_file == "correct.json":
            continue

        with pytest.raises(AssertionError):
            run_uncles_test(f"InvalidBlocks/bcUncleHeaderValidity/{test_file}")


@pytest.mark.parametrize(
    "test_file",
    os.listdir(
        "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
        "GeneralStateTests/stTransactionTest/"
    ),
)
def test_transactions(test_file: str) -> None:
    try:
        run_transaction_test(test_file)
    except KeyError:
        # Note The two tests below will raise KeyError
        # as these tests don't have tests for frontier.
        # Opcodes_TransactionInit_d33g0v0.json
        # Opcodes_TransactionInit_d127g0v0.json
        pass


@pytest.mark.parametrize(
    "test_file",
    os.listdir(
        "tests/fixtures/LegacyTests/Constantinople/BlockchainTests/"
        "GeneralStateTests/stRandom2"
    ),
)
def test_random2(test_file: str) -> None:
    try:
        run_random2_tests(test_file)
    except KeyError:
        pass
