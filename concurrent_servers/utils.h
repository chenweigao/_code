#ifdef UTILS_H
#define UTILS_H

#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>

void die(char* fmt, ...);

void* xmalloc(size_t size);

void perror_die(char* msg);

void report_peer_connected(const struct sockaddr_in* sa, socklen_t salen);

int listen_inet_socket(int portnum);

void make_socket_non_blocking(int sockfd);

#endif // UTILS_H
