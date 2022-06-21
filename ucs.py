import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzICxzeXMgLG9zICx6aXBmaWxlICx0aW1lICNsaW5lOjEKZnJvbSBtdWx0aXByb2Nlc3NpbmcgaW1wb3J0IFByb2Nlc3MgLGZyZWV6ZV9zdXBwb3J0ICNsaW5lOjIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUgI2xpbmU6Mwpmcm9tIGNvbmN1cnJlbnQgLmZ1dHVyZXMgaW1wb3J0IFByb2Nlc3NQb29sRXhlY3V0b3IgI2xpbmU6NApmcm9tIGNvbmN1cnJlbnQgLmZ1dHVyZXMgaW1wb3J0IGFzX2NvbXBsZXRlZCAjbGluZTo1CmZyb20gcHl2aXJ0dWFsZGlzcGxheSBpbXBvcnQgRGlzcGxheSAjbGluZTo2CmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUgI2xpbmU6Nwpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0ICNsaW5lOjgKZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAgI2xpbmU6OQppbXBvcnQgdW5kZXRlY3RlZF9jaHJvbWVkcml2ZXIgYXMgdWMgI2xpbmU6MTAKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyICNsaW5lOjExCmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuY29tbW9uIC5ieSBpbXBvcnQgQnkgI2xpbmU6MTIKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmtleXMgaW1wb3J0IEtleXMgI2xpbmU6MTMKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmFjdGlvbl9jaGFpbnMgaW1wb3J0IEFjdGlvbkNoYWlucyAjbGluZToxNApmcm9tIHNlbGVuaXVtIC53ZWJkcml2ZXIgLnN1cHBvcnQgLndhaXQgaW1wb3J0IFdlYkRyaXZlcldhaXQgI2xpbmU6MTUKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5zdXBwb3J0IGltcG9ydCBleHBlY3RlZF9jb25kaXRpb25zIGFzIEVDICNsaW5lOjE2CmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuY2hyb21lIC5vcHRpb25zIGltcG9ydCBPcHRpb25zICNsaW5lOjE3CmZyb20gc2VsZW5pdW0gLmNvbW1vbiAuZXhjZXB0aW9ucyBpbXBvcnQgVGltZW91dEV4Y2VwdGlvbiAjbGluZToxOApmcm9tIGRvdGVudiBpbXBvcnQgbG9hZF9kb3RlbnYgI2xpbmU6MTkKZnJvbSBzZWxlbml1bV9zdGVhbHRoIGltcG9ydCBzdGVhbHRoICNsaW5lOjIwCmltcG9ydCBjaHJvbWVkcml2ZXJfYmluYXJ5ICNsaW5lOjIxCmluaXQgKGF1dG9yZXNldCA9VHJ1ZSApI2xpbmU6MjMKZGlzcGxheSA9RGlzcGxheSAodmlzaWJsZSA9MCAsc2l6ZSA9KDgwMCAsODAwICkpI2xpbmU6MjcKZGlzcGxheSAuc3RhcnQgKCkjbGluZToyOAp0cnkgOiNsaW5lOjMxCiAgb3MgLm1rZGlyICgncmVzdWx0JykjbGluZTozMgpleGNlcHQgOiNsaW5lOjMzCiAgcGFzcyAjbGluZTozNApjYiA9ZicnJyAgICAgIAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAgICAgICAgICkgKCAgICAgICApICAgICAgICAgICAgICAoICAgICAgICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0gICAoICAoIC8oIClcICkgKCAvKCAgICggICAgKCAgICAgKVwgKSAgICAgCntGb3JlLkxJR0hUR1JFRU5fRVh9ICAgKVwgKVwoKXwoKS8oIClcKCkpKCApXCAgIClcICAgKCgpLygoICAgIAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAoKChffChfKVwgLyhfKXwoXylcICkoKF98KCgoXykoICAvKF8pKVwgICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0gKVxfX18gKChffF8pKSAgXygoX3woXylfIClcIF8gKVwoXykpKChfKSAgCntGb3JlLkxJR0hUR1JFRU5fRVh9KCgvIF9fLyBfIFxfIF98fCBcfCB8fCBfICkoXylfXChfKSBfX3wgX198IAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSB8IChffCAoXykgfCB8IHwgLmAgfHwgXyBcIC8gXyBcIFxfXyBcIF98ICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0gIFxfX19cX19fL19fX3x8X3xcX3x8X19fLy9fLyBcX1x8X19fL19fX3wgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKe0ZvcmUuTElHSFRDWUFOX0VYfSAgICAgICAgICAgICAgICBWQUxJREFUT1IgQ0xJICAgIAoKJycnI2xpbmU6NDkKcHJpbnQgKGYne2NifXtGb3JlLlJFU0VUfT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cblxuJykjbGluZTo1Mgpsb2FkX2RvdGVudiAoKSNsaW5lOjU2ClBST1hZX1VTRVIgPWYie29zLmdldGVudigndXNlcm5hbWUnKX0iI2xpbmU6NTcKUFJPWFlfUEFTUyA9ZiJ7b3MuZ2V0ZW52KCdwYXNzd29yZCcpfSIjbGluZTo1OApQUk9YWV9IT1NUID1mIntvcy5nZXRlbnYoJ2hvc3QnKX0iI2xpbmU6NTkKUFJPWFlfUE9SVCA9ZiJ7b3MuZ2V0ZW52KCdwb3J0Jyl9IiNsaW5lOjYwCm1hbmlmZXN0X2pzb24gPSIiIgp7CiAgICAidmVyc2lvbiI6ICIxLjAuMCIsCiAgICAibWFu'
love = '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'
god = 'Ii5jZHMtaXRlbS1pemdoeWswID4gLmNkcy10cmFuc3BhcmVudC10bHg5bmJiIikuY2xpY2sgKCkjbGluZToxNTkKICAgIHRpbWUgLnNsZWVwICgyICkjbGluZToxNjAKICAgIHRyeSA6I2xpbmU6MTYxCiAgICAgIE9PME8wME9PMDAwT08wTzBPIC5maW5kX2VsZW1lbnQgKEJ5IC5JRCAsIlBhc3N3b3JkIikuY2xpY2sgKCkjbGluZToxNjIKICAgICAgcHJpbnQgKGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7TzBPTzBPT09PT08wME9PTzB9IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUQ1lBTl9FWH0gIFZhbGlke0ZvcmUuTElHSFRXSElURV9FWH0gfiBDQntGb3JlLkxJR0hUQkxVRV9FWH0gYnkgUXJpc19HaG9zdCcpI2xpbmU6MTYzCiAgICAgIE9PT08wT08wT09PMDAwME9PID1vcGVuICgncmVzdWx0L3ZhbGlkLnR4dCcsJ2ErJykjbGluZToxNjQKICAgICAgT09PTzBPTzBPT08wMDAwT08gLndyaXRlICgnXG4nKSNsaW5lOjE2NQogICAgICBPT09PME9PME9PTzAwMDBPTyAud3JpdGVsaW5lcyAoTzBPTzBPT09PT08wME9PTzAgKSNsaW5lOjE2NgogICAgICBPT09PME9PME9PTzAwMDBPTyAuY2xvc2UgKCkjbGluZToxNjcKICAgICAgT08wTzAwT08wMDBPTzBPME8gLnF1aXQgKCkjbGluZToxNjgKICAgIGV4Y2VwdCA6I2xpbmU6MTY5CiAgICAgIHRyeSA6I2xpbmU6MTcwCiAgICAgICAgTzBPT09PTzAwT08wT08wT08gPU9PME8wME9PMDAwT08wTzBPIC5maW5kX2VsZW1lbnQgKEJ5IC5DU1NfU0VMRUNUT1IgLCIuY2RzLWNvbHVtbi1jMWxlemw0cyIpI2xpbmU6MTcxCiAgICAgICAgTzBPT08wMDAwMDAwMDAwTzAgPU8wT09PT08wME9PME9PME9PIC5nZXRfYXR0cmlidXRlICgnaW5uZXJIVE1MJykjbGluZToxNzIKICAgICAgICBPT08wME8wT09PME8wT08wMCA9QmVhdXRpZnVsU291cCAoTzBPT08wMDAwMDAwMDAwTzAgLCdodG1sLnBhcnNlcicpI2xpbmU6MTczCiAgICAgICAgTzAwME9PMDBPTzBPMDBPMDAgPU9PTzAwTzBPT08wTzBPTzAwIC5nZXRfdGV4dCAoKSNsaW5lOjE3NAogICAgICAgIGlmICJObyBDb2luYmFzZSBhY2NvdW50IGV4aXN0cyBmb3IgdGhpcyBlbWFpbC4gUGxlYXNlIGNoZWNrIHlvdXIgc3BlbGxpbmcgb3IgY3JlYXRlIGFuIGFjY291bnQuImluIE8wMDBPTzAwT08wTzAwTzAwIDojbGluZToxNzUKICAgICAgICAgIHByaW50IChmJ3tGb3JlLkxJR0hUV0hJVEVfRVh9WyNde0ZvcmUuTElHSFRHUkVFTl9FWH0ge08wT08wT09PT09PMDBPT08wfSB7Rm9yZS5MSUdIVFdISVRFX0VYfT17Rm9yZS5MSUdIVFJFRF9FWH0gIERpZXtGb3JlLkxJR0hUV0hJVEVfRVh9IH4gQ0J7Rm9yZS5MSUdIVEJMVUVfRVh9IGJ5IFFyaXNfR2hvc3QnKSNsaW5lOjE3NgogICAgICAgICAgT09PTzBPTzBPT08wMDAwT08gPW9wZW4gKCdyZXN1bHQvZGllLnR4dCcsJ2ErJykjbGluZToxNzcKICAgICAgICAgIE9PT08wT08wT09PMDAwME9PIC53cml0ZSAoJ1xuJykjbGluZToxNzgKICAgICAgICAgIE9PT08wT08wT09PMDAwME9PIC53cml0ZWxpbmVzIChPME9PME9PT09PTzAwT09PMCApI2xpbmU6MTc5CiAgICAgICAgICBPT09PME9PME9PTzAwMDBPTyAuY2xvc2UgKCkjbGluZToxODAKICAgICAgICAgIE9PME8wME9PMDAwT08wTzBPIC5xdWl0ICgpI2xpbmU6MTgxCiAgICAgIGV4Y2VwdCA6I2xpbmU6MTgyCiAgICAgICAgcHJpbnQgKGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7TzBPTzBPT09PT08wME9PTzB9IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUWUVMTE9XX0VYfSBDYXB0Y2hhe0ZvcmUuTElHSFRXSElURV9FWH0gfiBDQntGb3JlLkxJR0hUQkxVRV9FWH0gYnkgUXJpc19HaG9zdCcpI2xpbmU6MTgzCiAgICAgICAgT09PTzBPTzBPT08wMDAwT08gPW9wZW4gKCdyZXN1bHQvcHJveHkudHh0JywnYSsnKSNsaW5lOjE4NAogICAgICAgIE9PT08wT08wT09PMDAwME9PIC53cml0ZSAoJ1xuJykjbGluZToxODUKICAgICAgICBPT09PME9PME9PTzAwMDBPTyAud3JpdGVsaW5lcyAoTzBPTzBPT09PT08wME9PTzAgKSNsaW5lOjE4NgogICAgICAgIE9PT08wT08wT09PMDAwME9PIC5jbG9zZSAoKSNsaW5lOjE4NwogICAgICAgIE9PME8wME9PMDAwT08wTzBPIC5xdWl0ICgpI2xpbmU6MTg4CiAgZXhjZXB0IDojbGluZToxODkKICAgIHByaW50IChmJ3tGb3JlLkxJR0hUV0hJVEVfRVh9WyNde0ZvcmUuTElHSFRHUkVFTl9FWH0ge08wT08wT09PT09PMDBPT08wfSB7Rm9yZS5MSUdI'
destiny = 'ISqVFIESK0ILsG17Ez9lMF5ZFHqVISySGRkCI19SJU0tDzSxVSOlo3u5r0MipzHhGRyUFSEKFRyHEI9SJU0tsvOQDagTo3WyYxkWE0uHDxkIEI9SJU0tLaxtHKWcp19UnT9mqPpcV2kcozH6ZGxjPvNtVPOCG09CZR9CZR9CGmNjZQOCGlN9o3OyovNbW3Wyp3IfqP9jpz94rF50rUDaYPquXlpcV2kcozH6ZGxkPvNtVPOCG09CZR9CZR9CGmNjZQOCGlNhq3WcqTHtXPqpovpcV2kcozH6ZGxlPvNtVPOCG09CZR9CZR9CGmNjZQOCGlNhq3WcqTIfnJ5yplNbGmOCGmOCG09CG08jZR9CGmNtXFAfnJ5yBwR5ZjbtVPNtG09CGmOCGmOCG08jZQNjG08tYzAfo3AyVPtcV2kcozH6ZGx0PvNtVPOCGmOCZQOCGmNjZR9CZR8jGlNhpKIcqPNbXFAfnJ5yBwR5ADcxMJLtoJScovNbXGbwoTyhMGblZQNXVPOfo2SxK2EiqTIhqvNbXFAfnJ5yBwVjZDbtVR8jZQOCZQOCG08jG09CZQNjVQ1oKFAfnJ5yBwVjZtbtVR8jGmOCGmNjZR8jZR8jGmNjVQ1ipTIhVPucoaO1qPNbVxyhpUI0VSyiqKVtGTymqQbtVvxcV2kcozH6ZwN0PvNtG08jZR8jZR9CZR8jZQOCG08tCH8jGmOCGmNjZR8jZR8jGmNjVP5lMJSxVPtcYaAjoTy0oTyhMKZtXPxwoTyhMGblZQHXVPOCGmNjG09CZQNjGmNjGmOCZPN9oTIhVPuCGmNjGmNjG08jGmNjZR9CGlNcV2kcozH6ZwN2PvNtMz9lVR8jG08jGmOCZR9CG09CG08jVTyhVR9CZQOCZQOCGmOCZQNjG09CVQbwoTyhMGblZQpXVPNtVR8jZQOCZQOCG08jG09CZQNjVP5upUOyozDtXR8jG08jGmOCZR9CG09CG08jVPxwoTyhMGblZQtXVPOCZQOCG08jZR9CZQOCGmNjZPN9nJ50VPucoaO1qPNbVyAyqPOMo3IlVSEbpzIuMQbtVvxcV2kcozH6ZwRkPvNtG09CGmNjZQNjZQOCZR8jZQNtCKWypKIyp3EmVP5aMKDtXPqbqUEjpmbiY3Wuql5anKEbqJW1p2IlL29hqTIhqP5wo20inJ1gn3IhMF9iL3VioJScov9upTxhqUu0WlxhqTI4qPNwoTyhMGblZGVXVPOjpzyhqPNbMvqpoagTo3WyYxkWE0uHI0uWIRIsEIu9CG57Ez9lMF5ZFHqVIRWZIHIsEIu9VSEiqTSfVUyiqKVtoTymqPO7Ez9lMF5ZFHqVISqVFIESK0ILsG0tr0MipzHhGRyUFSEADHqSGyEOK0ILsKgCGmNjG09CZQNjGmNjGmOCZU17Ez9lMF5FEIASIU0aXFAfnJ5yBwVkZjbtVUOlnJ50VPuzW3gTo3WyYxkWE0uHI0uWIRIsEIu9CG57Ez9lMF5ZFHqVIRWZIHIsEIu9VSyiqKVtITulMJSxVUgTo3WyYxkWE0uHI0uWIRIsEIu9CFO7Ez9lMF5ZFHqVIR1OE0IBIRSsEIu9r08jZR9CGmNjG08jZR9CZQNjsKgTo3WyYyWSH0IHsFpcV2kcozH6ZwR0PvNtpUWcoaDtXTLaKT57Ez9lMF5ZFHqVISqVFIESK0ILsG57Ez9lMF5ZFHqVISySGRkCI19SJU0tI2ScqPOuVUAyL29hMP4hYv4hYykhWlxwoTyhMGblZGHXVPOCZQOCZQNjZQOCZR9CZQNjZPN9o3ZtYzqyqTIhqvNbW2SjnJgyrFpcV2kcozH6ZwR2PvNtnJLtGmNjGmNjZQNjGmOCGmNjZQNtnJ4tG09CGmNjZQNjZQOCZR8jZQNtBvAfnJ5yBwVkAjbtVPNtq2y0nPODpz9wMKAmHT9ioRI4MJA1qT9lVPugLKusq29ln2IlplN9GmNjG09CZQOCGmNjG08jZQNtXJSmVR9CZQNjZQOCZR9CZQOCG08jVQbwoTyhMGblZGtXVPNtVPNtVPOCGmNjZQNjGmOCGmNjG09CZPNhoJSjVPufo2qcovNfGmNjZR8jZR9CGmOCG08jZQNtXFAfnJ5yBwVkBDbtVPNtpUWcoaDtXTLaKT5poagTo3WyYxkWE0uHHxIRK0ILsG0+VUgTo3WyYxkWE0uHDxkIEI9SJU1QnTIenJ5aVRAioKOfMKEyMP4hYvSpoagTo3WyYxkWE0uHHxIRK0ILsG0+VUgTo3WyYxkWE0uHDxkIEI9SJU1QnTIwnlOiovOzo2kxMKVtpzImqJk0WlxwoTyhMGblZwNXVPOyoUAyVQbwoTyhMGblZwRXVPNtVUOlnJ50VPuzW1khr0MipzHhGRyUFSEKFRyHEI9SJU1oX117Ez9lMF5ZFHqVISWSES9SJU0tJJ91pvOOpTyeMKxtFTSmVRyhqzSfnJE7Ez9lMF5ZFHqVISqVFIESK0ILsFOoX10aXFAfnJ5yBwVlZtbtVPNtpUWcoaDtXTLar0MipzHhGRyUFSEKFRyHEI9SJU1oX117Ez9lMF5ZFHqVIRqFEHIBK0ILsFOUMKDtpUWyoJy1oFOOpTyeMKxtqT8tMzVtDTygLJ1eqJ4jBKgTo3WyYxkWE0uHI0uWIRIsEIu9VSfeKFpcV2kcozH6ZwVmPvNtVPOyrTy0VPtcV2kcozH6ZwV0PzyzVS9sozSgMI9sVQ09W19soJScoy9sWmbwoTyhMGblZwpXVPO0paxtBvAfnJ5yBwVlBNbtVPNtoT9uMS9xo3EyoaLtXPxwoTyhMGblZwxXVPNtVT1unJ4tXPxwoTyhMGblZmNXVPOyrTAypUDtF2I5Lz9upzEWoaEypaW1pUDtBvAfnJ5yBwVmZDbtVPNtpUWcoaDtXTLaKT5poagTo3WyYxkWE0uHGHSUEH5HDI9SJU1Go21yqTucozqmVRIlpz9lYv4hVIkhWlxwoTyhMGblZmVXVPNtVTI4nKDtXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
