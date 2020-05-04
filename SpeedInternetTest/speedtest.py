import speedtest

test = speedtest.SpeedTest()
download = test.download()
upload = test.upload()

print(f"Download speed: {download}\n Upload speed: {upload}")
