from PIL import ImageDraw

class RemoteDraw:
    def __init__(self, image, *args, **kwargs):
        # IMPORTANT : utiliser le Draw original
        self._real_draw = ImageDraw._original_Draw(image, *args, **kwargs)

    # --- interception TEXT ---
    def text(self, position, text, *args, **kwargs):
        print(f"[DRAW TEXT] {text} at {position}")
        return self._real_draw.text(position, text, *args, **kwargs)

    # --- interception LINE ---
    def line(self, coords, *args, **kwargs):
        print(f"[DRAW LINE] {coords}")
        return self._real_draw.line(coords, *args, **kwargs)

    # --- interception RECT ---
    def rectangle(self, coords, *args, **kwargs):
        print(f"[DRAW RECT] {coords}")
        return self._real_draw.rectangle(coords, *args, **kwargs)

    # --- interception BITMAP ---
    def bitmap(self, position, bitmap, *args, **kwargs):
        print(f"[DRAW BITMAP] at {position}")
        return self._real_draw.bitmap(position, bitmap, *args, **kwargs)

    # --- fallback automatique ---
    def __getattr__(self, name):
        return getattr(self._real_draw, name)
