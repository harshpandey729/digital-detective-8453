# Mission 7 - How computers communicate

## 1. Task / objective
Explain LAN, MAN, WAN, DNS, routers, protocols, packet switching and client-server communication.

## 2. Work completed
Documented network concepts, performed public HTTPS and DNS checks, and described the steps a browser follows when opening a website.

## 3. Commands / tools used
- `curl -sS -I --max-time 10 https://example.com`: returned `HTTP/2 200`.
- Python 3.9.6 `socket.getaddrinfo("example.com", 443, type=socket.SOCK_STREAM)`: resolved two unique addresses; address values are omitted.

### Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | A network covering a small location | Home or lab |
| MAN | A network covering a city or large campus | University campus network |
| WAN | A network spanning broad geographical areas | The internet |
| DNS | Resolves a domain name into network addresses | `example.com` lookup |
| Router | Forwards network traffic between networks | Home or campus router |
| Protocol | A shared set of communication rules | HTTP/HTTPS or TCP/IP |
| Packet switching | Splits data into packets that can be forwarded independently | Web page data divided into packets |
| Client-server | A client requests a service and a server responds | Browser requesting a website |

### Connectivity observations

The HTTPS request received `HTTP/2 200`, confirming that the example host responded successfully. The DNS lookup succeeded and returned two unique address values; they are not recorded here. A connectivity test checks whether a host can be reached and respond. DNS resolves a human-readable domain name to network address information.

### Website communication

1. The browser acts as a client and receives the website address.
2. The browser sends the domain to DNS to resolve an address.
3. DNS returns the matching network address information.
4. The browser uses the router and internet to send a request.
5. The networking stack divides data into packets. Network protocols define how these packets are addressed, transmitted, and interpreted.
6. The server receives it and returns a response containing page resources.
7. The browser interprets the response and displays the website.

## 4. My understanding
Networks connect devices, DNS translates names, routers forward traffic, protocols define communication rules and packet switching allows data to travel efficiently.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Used public example domains and recorded no private network details.

## 7. Evidence / files
Network concept table, observed HTTPS and DNS results, and privacy-safe website communication steps in this README.

## 8. Commit details
Commit message: `Explain networking concepts and website communication`
