from .ssd_1b_loader import CheckpointLoaderSimple

NODE_CLASS_MAPPINGS = {
    "SSD-1B-Loader": CheckpointLoaderSimple,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SSD-1B-Loader": "SSD-1B-Loader",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]