import os
import os.path
import re
import sys
import gradio as gr
from modules import scripts

class Script(scripts.Script):
    def title(self):
        return "Session Organizer"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion(self.title(), open=False):
                with gr.Row():
                    session_name = gr.Textbox("", label="Session Name", placeholder="Output subfolder name, leave blank to disable")

        return [session_name]

    def process(self, p, session_name):
        if not session_name.strip():
            return

        print(f"[SessionOrganizer] Saving outputs to '{session_name}' subfolder")

        if p.outpath_samples:
            p.outpath_samples = os.path.join(p.outpath_samples, "sessions", session_name)
            os.makedirs(p.outpath_samples, exist_ok=True)
        if p.outpath_grids:
            p.outpath_grids = os.path.join(p.outpath_grids, "sessions", session_name)
            os.makedirs(p.outpath_grids, exist_ok=True)
