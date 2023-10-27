import comfy
import folder_paths

import comfy.supported_models as supported_models
import comfy.ldm.modules.diffusionmodules.openaimodel as openaimodel
import comfy.model_base
from .openaimodel import ConvertedUNetModel

import importlib

class SDXL(supported_models.SDXL):
    unet_config = {
        "model_channels": 320,
        "use_linear_in_transformer": True,
        "transformer_depth": [0, 2, 4], # max depth of input_blocks
        "context_dim": 2048,
        "adm_in_channels": 2816
    }

class CheckpointLoaderSimple:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                             }}
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "ssd-1b"

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        OrgUNetModel = openaimodel.UNetModel
        OrgSDXL = supported_models.SDXL

        openaimodel.UNetModel = ConvertedUNetModel
        supported_models.models[5] = SDXL

        importlib.reload(comfy.model_base)
        
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        
        openaimodel.UNetModel = OrgUNetModel
        supported_models.models[5] = OrgSDXL
        importlib.reload(comfy.model_base)
        
        return out[:3]