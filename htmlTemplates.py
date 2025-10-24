import base64

css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="not.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

# bot template
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_base64 = get_base64_image("not.png")

bot_template = f'''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,{image_base64}" alt="bot Avatar">
    </div>    
    <div class="message">{{{{MSG}}}}</div>
</div>
'''

# user template
image2 = get_base64_image("me.png")

user_template = f'''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,{image2}" alt="User Avatar">
    </div>    
    <div class="message">{{{{MSG}}}}</div>
</div>
'''