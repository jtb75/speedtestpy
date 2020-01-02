import subprocess
result = subprocess.check_output(['/usr/local/bin/speedtest-cli'])
result = result.decode('utf-8')
result = result.split('\n')

result[4] = result[4].split('Hosted by ', 1)[-1]
(host, remainder) = result[4].split(' [')
(distance, pingspeed) = remainder.split(']: ')
distance = distance.split()
pingspeed = pingspeed.split()

download = result[6].split()
download.pop(0)

upload = result[8].split()
upload.pop(0)
