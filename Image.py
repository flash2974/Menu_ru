from PIL import Image, ImageDraw, ImageFont

# Crée une image blanche
image = Image.new('RGB', (720, 1280), color = (0, 0, 0))

# Initialise l'objet ImageDraw
draw = ImageDraw.Draw(image)

# Définir la police et la taille (si vous n'avez pas de police spécifique, vous pouvez ignorer)
# Vous pouvez également télécharger une police personnalisée si nécessaire
font = ImageFont.truetype('arial.ttf', 40)

# Ajouter du texte sur l'image
text = "Bonjour, PIL!"
position = (120, 100)  # Position du texte (x, y)
text_color = (255, 255, 255)  # Couleur du texte (noir ici)

# Dessiner le texte
draw.text(position, text, fill=text_color, font=font, align="center", embedded_color=True)

# Sauvegarder l'image avec le texte
image.save('image_avec_texte.png')
