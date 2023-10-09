# BGF-YOLO based on Ultralytics YOLOv8x 8.0.109 object detection model with same license, AGPL-3.0 license
"""
Import modules. Visualize with:

from nn.modules import *
import torch
import os

x = torch.ones(1, 128, 40, 40)
m = Conv(128, 128)
f = f'{m._get_name()}.onnx'
torch.onnx.export(m, x, f)
os.system(f'onnxsim {f} {f} && open {f}')
"""

from .block import (C1, C2, C3, C3TR, DFL, SPP, SPPF, Bottleneck, BottleneckCSP, C2f, C3Ghost, C3x, GhostBottleneck,
                    HGBlock, HGStem, Proto, RepC3, se_block, cbam_block, eca_block, CA_Block, CSPStage,
                    BiLevelRoutingAttention)
from .conv import (CBAM, ChannelAttention, Concat, Conv, Conv2, ConvTranspose, DWConv, DWConvTranspose2d, Focus,
                   GhostConv, LightConv, RepConv, SpatialAttention)
from .head import Classify, Detect, Pose, RTDETRDecoder, Segment
from .transformer import (AIFI, MLP, DeformableTransformerDecoder, DeformableTransformerDecoderLayer, LayerNorm2d,
                          MLPBlock, MSDeformAttn, TransformerBlock, TransformerEncoderLayer, TransformerLayer)

__all__ = [
    'Conv', 'Conv2', 'LightConv', 'RepConv', 'DWConv', 'DWConvTranspose2d', 'ConvTranspose', 'Focus', 'GhostConv',
    'ChannelAttention', 'SpatialAttention', 'CBAM', 'Concat', 'TransformerLayer', 'TransformerBlock', 'MLPBlock',
    'LayerNorm2d', 'DFL', 'HGBlock', 'HGStem', 'SPP', 'SPPF', 'C1', 'C2', 'C3', 'C2f', 'C3x', 'C3TR', 'C3Ghost',
    'GhostBottleneck', 'Bottleneck', 'BottleneckCSP', 'Proto', 'Detect', 'Segment', 'Pose', 'Classify',
    'TransformerEncoderLayer', 'RepC3', 'RTDETRDecoder', 'AIFI', 'DeformableTransformerDecoder',
    'DeformableTransformerDecoderLayer', 'MSDeformAttn', 'MLP','se_block','cbam_block','eca_block','BiLevelRoutingAttention','CA_Block','CSPStage']
