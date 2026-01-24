; Finux Kernel: Frost Protocol Block Reward Interrupt Handler (x86_64)
; Target: 3-Second Deterministic Heartbeat

section .text
extern frost_consensus_broadcast    ; C/Python bridge for state sync
extern ase_sign_block               ; Aluminium Secure Enclave signing

global frost_irq_handler

frost_irq_handler:
    push rbp
    mov rbp, rsp
    pushall                         ; Save all registers to preserve agent state

    ; 1. Clear the Local APIC Interrupt
    mov rax, [apic_base_addr]
    mov dword [rax + 0xB0], 0       ; EOI (End of Interrupt)

    ; 2. Time-Critical: Sign the 3s Block
    ; We call the ASE directly from Assembly to skip Python latency
    call ase_sign_block

    ; 3. Trigger Frostnerjo Node Broadcast
    ; This sends the FrosTether.sol state updates to the network
    call frost_consensus_broadcast

    ; 4. Resume AI Agent Execution
    popall
    pop rbp
    iretq                           ; Return to the interrupted Python agent
; Finux Vision Gate: Secure Hologram Buffer Lock
; Prevents non-kernel apps from intercepting the raw private key

global secure_scan_init

secure_scan_init:
    ; 1. Lock the Camera Buffer to the Finux Kernel
    mov rax, 0x01          ; SYSCALL_LOCK_HARDWARE
    mov rdi, [cam_id]      ; Meta Quest Passthrough ID
    syscall

    ; 2. Run Diffraction Check (PQC Lattice)
    ; This calls the Assembly-optimized PQC module
    call verify_hologram_lattice
    
    ; 3. If Valid, move Key to Secure Enclave
    jz .failed_verify
    mov rsi, [raw_key_buffer]
    call ase_move_to_vault  ; Move to Aluminium Secure Enclave
    
    ret
