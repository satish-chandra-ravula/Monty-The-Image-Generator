from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import torch


model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"

pipe = StableDiffusionPipeline.from_pretrained(model_id1, torch_dtype=torch.float16)
pipe = pipe.to("cuda")


prompt = """A boy playing with shark in the sea.
"""


image = pipe(prompt).images[0]


print("[PROMPT]: ",prompt)
plt.imshow(image);
plt.axis('off');