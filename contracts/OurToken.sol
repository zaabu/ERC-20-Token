// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity <0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

//ERC20 provides standard implementation for creating / working with erc tokens
contract OurToken is ERC20 {
    constructor(uint256 initialSupply) public ERC20("Bright", "BRGHT") {
        //creating an initialSupply of tokens, which will be assigned to the address that deploys the contract.
        _mint(msg.sender, initialSupply);
    } 
}