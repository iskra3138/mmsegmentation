# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class DALESDataset(CustomDataset):
    """DALES2D10 dataset.

    In segmentation map annotation for DALES dataset, 0,9 are the ignore index.
    ``reduce_zero_label`` should be set to True. The ``img_suffix`` and
    ``seg_map_suffix`` are both fixed to '.png'.
    """
    CLASSES = ('Unknown', 'ground', 'vegetation', 'cars', 'trucks', 'power_lines', 'fences',
               'poles', 'building', 'no_point')

    PALETTE = [[0, 0, 139],  # Unknown -> dark blue
          [0, 0, 255],  # ground -> blue
          [0, 100, 0],  # vegetation -> Dark Green
          [255, 192, 203],  # cars -> pink
          [255, 255, 0],  # trucks -> yellow
          [144, 238, 144],  # power lines -> light green
          [173,216,230],  # fences ->  light blue
          [255,165,0],  # poles  ->  orange
          [255, 0, 0],  # building -> red
          [255,255,255] # no point -> white
          ]
    def __init__(self, **kwargs):
        super(DALESDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            ignore_index=9,
            reduce_zero_label=True,
            **kwargs)
