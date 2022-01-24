// SPDX-License-Identifier: MIT
pragma solidity ^0.8.11;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract UmarToken is ERC20 {
    constructor(uint256 initialSupply) public ERC20("UmarToken", "UMR") {
        _mint(msg.sender, initialSupply);
    }
}