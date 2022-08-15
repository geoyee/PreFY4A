from .FY4A.codes.fy4a import FY4A
from .FY4A.codes.components import Arg
from .FY4A.codes.utils import gen_lat_lon
import os
import os.path as osp


new_lon, new_lat = gen_lat_lon(
    62.0000000000000000, 
    105.0018536015601001, 
    46.0003889722701871, 
    26.0000000012110064, 
    0.005086568914308031708
)


def _mkdir(dir: str) -> None:
    if not osp.exists(dir):
        os.makedirs(dir)


def readL2CLM(file_path: str, save_dir: str) -> None:
    fy4a = FY4A(Arg().arg_parse('-d'.split()))
    file_name = file_path.replace("\\", "/").split("/")[-1]
    _mkdir(save_dir)
    sv_path = osp.join(save_dir, file_name.replace(".NC", ".tif").replace(".nc", ".tif"))
    fy4a.get_data_from_data_name(file_path, 'CLM', new_lon, new_lat, sv_path=sv_path)


def readL1FDI4K(file_path: str, save_dir: str) -> None:
    fy4a = FY4A(Arg().arg_parse('-d'.split()))
    file_name = file_path.replace("\\", "/").split("/")[-1]
    _mkdir(save_dir)
    sv_path = osp.join(save_dir, file_name.replace(".HDF", ".tif").replace(".hdf", ".tif"))
    fy4a.get_data_from_4k_fdi(file_path, new_lon, new_lat, sv_path=sv_path)
