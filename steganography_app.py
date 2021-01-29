import streamlit as st
from PIL import Image
import stepic

st.header("Steganography Encoder and Decoder")
st.write("")
st.write("")
st.write("")

def agreement():
    text = st.beta_expander("Agreement", expanded = 1)
    with text:
        st.write("This application enables the user to encode and decode written messages within images.")
        global confirm_agree
        confirm_agree = st.checkbox("Check this box to confirm you will not use this application \
        to assist in any illegal activities. Where the definition of illegal activities may differ depending on the \
        the location from which you are using this application. In some regions encryption may be illegal, \
        do not use this application if encryption is forbidden.")
    if confirm_agree == 1:
        st.write("")
        main()

def main():
    mode = st.selectbox("Would you like to encode or decode a message?", ("Encode", "Decode"))
    encode_pic = "Image to encode"
    decode_pic = "Image to decode"

    if mode == "Encode":
        image_encode = st.file_uploader(encode_pic, type = ['PNG','jpg','JPEG'])
        if image_encode != None:
            image_encode = Image.open(image_encode)
            message_encode = st.text_input("Enter your message")
            text_for_pic = str.encode(message_encode)
            confirm_encode = st.checkbox("Confirm message and encode")

            if message_encode != "" and confirm_encode == 1:
                encoded_image = stepic.encode(image_encode,text_for_pic)
                st.write("Message encoded sucessfully")
                #st.write("You encoded the following message:")
                #st.write(message_encode)
                Path = st.text_input("Enter the destination path for the saved image")
                image_name = st.text_input("What name would you like the new image to be saved as?")
                png = ".png"
                backslash = "\\"
                paste = Path+backslash+image_name+png
                save_image = st.checkbox("Save your encoded message")

                if save_image == 1:
                    encoded_image.save(paste,mode = 'r',formats = 'png')
                    st.write("The encoded image below has been saved as a png to: **{}**".format(paste))
                    st.image(encoded_image, use_column_width = True)

    else:
        image_decode = st.file_uploader(decode_pic, type = ['PNG'])
        if image_decode != None:
            image_decode = Image.open(image_decode).convert(mode='RGB')
            decoded_image = stepic.decode(image_decode)
            confirm_decode = st.checkbox("Decode the message")
            if confirm_decode == 1:
                st.write("")
                st.write("**The hidden message is:** {}".format(decoded_image))
                st.image(image_decode,use_column_width = True)

agreement()
