#include "cpp-httplib/httplib.h"
#include <iostream>

int main() {
  std::cout << "Woher ich wohl diese Info habe?: " << std::endl;

  httplib::Client client{"http://bbzwchallenge.k8s.firenet.ch"};
  auto res = client.Get("/wYhig");

  if (!res) {
    std::cerr << res.error() << std::endl;
    return 1;
  } else {
    std::cout << res->body << std::endl;
    return 0;
  }
}
