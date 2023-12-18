import os
import pytest


@pytest.fixture
def sample_data():
    # Create sample data for testing
    data = [
        '00COTAHIST.2022BOVESPA 20221229                                                                                                                                                                                                                      ',
        '012022010302GNDI3       010INTERMEDICA ON      NM   R$  000000000597000000000060880000000005727000000000589600000000058750000000005873000000000587520535000000000003960200000000023351263100000000000000009999123100000010000000000000BRGNDIACNOR2103',
        '012022010302ABEV3       010AMBEV S/A   ON           R$  000000000154200000000015540000000001515000000000152900000000015330000000001532000000000153343784000000000023833600000000036454098800000000000000009999123100000010000000000000BRABEVACNOR1125',
        '012022010302MODL11      010MODALMAIS   UNT     N2   R$  000000000108000000000011470000000001071000000000110800000000010930000000001093000000000111103729000000000000725000000000000803365000000000000000009999123100000010000000000000BRMODLCDAM13103',
        '012022010302TASA4       010TAURUS ARMASPN      N2   R$  000000000250000000000025050000000002428000000000246600000000024540000000002449000000000245402665000000000000610900000000001506876600000000000000009999123100000010000000000000BRTASAACNPR4100',
        '012022010302CRIV4       010ALFA FINANC PN           R$  000000000056800000000005700000000000557000000000056800000000005700000000000557000000000057000010000000000000005800000000000003296500000000000000009999123100000010000000000000BRCRIVACNPR1206'
    ]
    with open("sample_data.txt", "w") as file:
        file.write("\n".join(data))

    
    
    yield

    # Clean up the sample data file
    os.remove("sample_data.txt")
    
# @pytest.fixture(scope='module')
# def metadata_fixture():
#     # Load the metadata from metadata.toml
#     metadata_data = tomllib.loads(open("metadata.toml").read(), decoder="utf-8")

#     # Create a MetaData instance with the loaded data
#     metadata = MetaData(metadata_data)
    
#     yield metadata