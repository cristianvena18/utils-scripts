import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print("Download speed: ", download)
print("Upload speed: ", upload)
