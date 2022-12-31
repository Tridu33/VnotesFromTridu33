






https://guix.gnu.org/manual/zh-cn/html_node/Zai-Xu-Ni-Ji-Li-Yun-Xing-Guix.html
 

```
qemu-system-x86_64 \
   -nic user,model=virtio-net-pci \
   -enable-kvm -m 1024 \
   -device virtio-blk,drive=myhd \
   -drive if=none,file=/tmp/qemu-image,id=myhd
```





# GuixSD

截至 1.3.0 版本，独立的 Guix 系统可以安装 在 i686、x86_64、ARMv7 或 AArch64 架构的机器上。 它使用 Linux-Libre 内核和 GNU Shepherd init 系统。此外， GNU Guix 可以作为额外的包管理器安装在 Linux 内核的系统上。https://guix.gnu.org/download/