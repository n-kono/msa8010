# MSA 8010: Data Programming
## View Slides
To view slides, using `conda`:
1. Create a new environment (for example, _msa8010_), with `requirements.txt`:
    `conda create --name msa8010 python=3.8 --file requirements.txt`
    `conda activate`

1. Run a Jupyter file in slide mode. You have two options:
    1. Use RISE package _(recommended)_
    2. Use nbconvert. For example, to show  _03-NumpyPandas.ipynb_ slides: `jupyter nbconvert 03-NumpyPandas.ipynb --to slides --post serve`

## Modify
You can modify this repo and send pull requests.
### Personal Access Token (PAT)
You might need to create PAT on github.com to push local changes into your GitHub repository. 
On github.com:
1. Settings
1. Developer Settings
1. Personal access tokens
1. Generate new token

Then, you can treat the token similar to a password. However, since tokens are long texts you need to store them in a safe place such as a password manager (e.g., [1Password](https://1password.com/), [Bitwarden](https://bitwarden.com/), and [PassPack](https://www.passpack.com/)). Alternatively, you can use local password managers such as [KeepassXC](https://keepassxc.org/) and sync your passwords between your devices with [Syncthing](https://syncthing.net/).

By adding tokens in OS credential storages, you only enter the token once and while the token is valid, GitHub operations use that stored credential. First, visit [Git Credential Manager Core](https://github.com/microsoft/Git-Credential-Manager-Core/) and install the tool. Then, based on the OS, set the credential manager.

- Windows 10:
`git config --global credential.helper manager-core`.

- Mac:
Visit [Updating credentials from the macOS Keychain](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain)

- Linux:
`git config --global credential.helper store` (plain text, without GCM)