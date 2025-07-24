import requests

url = "https://www.amazon.in/GIGABYTE-NVIDIA-GeForce-WINDFORCE-Graphics/dp/B0C8ZQTRD7/ref=sr_1_2?crid=3EQJ7DXU8R5XD&dib=eyJ2IjoiMSJ9.G8su9C2AcstbOwzUZ1uw-6aYuRp3IP6GpYsjT5HhRudP68jg47-ri79xvvsQaV5DR6tPjBpn0SEftLbsyO4dxGu39iyiocVUdoE5cfZ3G-xtyeE8mAbaGFeG-PxuWF_JFC0oJxI2E4nxS9Oa2vfuLvGeT041mbBCxwKsbJROYqPbmU_azicFi7OFSGAduOzWwtmjBJrJkEAdM7poX8nv6x2sUlIjN8HpgyXxxOdmoGc.p5q5RRJG6Qal2GSqP_LtRiPD90_DwHVBs1iRtjJyIUA&dib_tag=se&keywords=rtx+4060&qid=1753371809&sprefix=rtx+4060%2Caps%2C243&sr=8-2"

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()

with open("tracker.html", "w") as file:
    file.write(response.text)