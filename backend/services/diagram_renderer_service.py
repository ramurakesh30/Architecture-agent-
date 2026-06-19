import subprocess


class DiagramRendererService:
    def render(self, mermaid_text, output_png):

        mermaid_file = output_png.replace(".png", ".mmd")
        with open(mermaid_file, "w") as f:
            f.write(mermaid_text)
        print("Rendering Mermaid:", mermaid_file)
        subprocess.run(
            [
                r"C:\Users\ramu rakesh\AppData\Roaming\npm\mmdc.cmd",
                "-i",
                mermaid_file,
                "-o",
                output_png,
            ],
            check=True,
        )
        print("Generated:", output_png)
        return output_png
