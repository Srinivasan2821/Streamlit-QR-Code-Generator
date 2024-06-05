import io
import segno
from PIL import Image
import streamlit as st

# Input for the name/text to generate QR code
test = st.text_input('Enter the Name')

if st.button("Show QR") and test:
    qr = segno.make_qr(test)
    qr_bytes = io.BytesIO()
    qr.save(qr_bytes, kind='png', scale=5)
    qr_bytes.seek(0)  # Move to the start of the BytesIO object
    qr_image = Image.open(qr_bytes)
    st.image(qr_image, caption='QR Code')

    # Prepare the QR code for download
    qr_bytes.seek(0)  # Move to the start of the BytesIO object again for download
    st.download_button(label="Download QR Code",
                       data=qr_bytes,
                       file_name=f"{test}.png",
                       mime="image/png")
