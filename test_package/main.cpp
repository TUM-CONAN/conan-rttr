#include <iostream>
#include <string>

#include "plasma/client.h"
#include "plasma/common.h"
#include "plasma/test-util.h"

int main(){
  plasma::ObjectID object_id = plasma::random_object_id();
  std::cout<<"ObjectID" << object_id.hex() << std::endl;
  return 0;
}