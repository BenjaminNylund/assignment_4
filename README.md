# Assignment 4 - Infiltrating the Government in an Alternative Universe

- [ ] Vulnerable Function Used to Evaluate Password
- [x] Intranet: Level 1
- [ ] Intranet: Level 2
- [ ] SSH
- [ ] Dropbox

## Hints

### Vulnerable Function Used to Evaluate Password

Hint:  det er en bug i timing attacket. Dere får ut 15 av 17. De siste to karakterene i passordet er 23

The following function is used to evaluate passwords:

```c++
int total_time = 0;

if (a.length() != b.length()) {
    return total_time;
}

for (size_t i = 0; i <= a.length(); ++i) {
    total_time++;

    if (a[i] != b[i]) {
        return total_time;
    }
}
return total_time;
```

### Intranet: Level 1

- Jonas Dahl frequently logs in to check his Wireguard credentials.
- Discord WEBHOOKS can be very useful here.
- Consider using the webhook to send data to yourself when Jonas Dahl logs in.
- Keep an eye out for information about Jonas' supervisor. She might have more access than Jonas.

### Intranet: Level 2

- You need to access the network on Wireguard. You'll retrieve this on Intranet: Level 1.
- `nmap` is a great tool for service discovery. Perhaps you can check which ports are open?

### SSH

- The SSH Server only accepts public-key authentication. You need to do something before accessing this server. What if we could overwrite the `authorized_keys` file somehow?
- Use ssh-rsa keys.

### Internal Network:
- 10.13.13.254 might have something interesting
- nmap -p 22 10.13.13.0/24

### Dropbox

- Consider how Dropbox could be used to gain access to SSH.
