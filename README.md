# MSA 8010: Data Programming

## Personal Access Token (PAT)
You need to create PAT on github.com to push local changes into your GitHub repository. 
On github.com:
1. Settings
1. Developer Settings
1. Personal access tokens
1. Generate new token

Then, you can treat the token similar to a password. However, since tokens are long texts you need to store them in a safe place such as a password manager (e.g., [1Password](https://1password.com/), [Bitwarden](https://bitwarden.com/), and [PassPack](https://www.passpack.com/)). Alternatively, you can use local password managers such as [KeepassXC](https://keepassxc.org/) and sync your passwords between your devices with [Syncthing](https://syncthing.net/).

By adding tokens in OS credential storages, you only enter the token once and while the token is valid, GitHub operations use that stored credential. 

- Windows 10:
`git config --global credential.helper manager-core`.
Visit [Git Credential Manager Core](https://github.com/microsoft/Git-Credential-Manager-Core/) if the command did not work.

- Mac:
Visit [Updating credentials from the macOS Keychain](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain)

- Linux:
`git config --global credential.helper store`