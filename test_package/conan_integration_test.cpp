#include <iostream>
#include "secp256k1_extrakeys.h"

int main() {
    secp256k1_context *vrfy;
    vrfy = secp256k1_context_create(SECP256K1_CONTEXT_VERIFY);
    if (vrfy) {
#ifdef NDEBUG
        std::cout << "secp256k1 Release test is passed." <<std::endl;
#else
        std::cout << "secp256k1 Debug test is passed." <<std::endl;
#endif
    }
}
