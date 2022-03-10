pragma solidity ^0.7.6;

contract greeter_contract {
    string greeter;

    function setGreet(string greetMesssage) public {
        greeter = greetMessage;
    }

    function getGreet() public returns(string memory) {
        return greeter;
    }

}
