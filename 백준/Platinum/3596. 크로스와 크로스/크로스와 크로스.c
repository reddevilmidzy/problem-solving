// Generated with https://github.com/boj-rs/basm-rs
// Learn rust (https://doc.rust-lang.org/book/) and get high performance out of the box!

// SOLUTION BEGIN
/*
use basm::platform::io::{Print, Reader, ReaderTrait, Writer};

pub fn main() {
    let mut reader: Reader = Default::default();
    let mut writer: Writer = Default::default();
    let n = reader.u32();

    let grundy = [
        6, 12, 22, 30, 32, 44, 54, 64, 76, 86, 98, 110, 118, 130, 132, 162, 170, 184, 194, 202,
        282, 290, 302, 356, 1046,
    ];

    if !grundy.contains(&n) {
        writer.print("1");
    } else {
        writer.print("2");
    }
}
*/
// SOLUTION END

// LOADER BEGIN
#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#include <Windows.h>
#include <io.h>
#elif defined(__linux__)
#include <unistd.h>
#ifndef MAP_ANONYMOUS
#define MAP_ANONYMOUS 0x20
#endif
#else
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif
#ifdef DEBUG
#include <stdio.h>
#endif

#ifndef UINT32_MAX
typedef unsigned char uint8_t;
typedef unsigned int uint32_t;
typedef unsigned long long uint64_t;
#endif

// Use cdecl on x86 (32bit), Microsoft x64 calling convention on amd64 (64bit)
#if defined(__LP64__) // LP64 machine, OS X or Linux
#define BASMCALL __attribute__((ms_abi))
#elif defined(_WIN64) // LLP64 machine, Windows
#if defined(_MSC_VER)
#define BASMCALL
#else
#define BASMCALL __attribute__((ms_abi))
#endif
#else // 32-bit machine, Windows or Linux or OS X -> forbid compilation
#error "The current file can only be compiled for amd64."
#define BASMCALL
#endif

void b91tobin(void *dest, char const *src) {
    uint8_t *p = (uint8_t *)dest;
    uint32_t eax = 0x1f;
    while (1) {
        while (*src == '\0') src++;
        uint32_t x = (uint32_t) *src++;
        if (x < 0x24) return;
        while (*src == '\0') src++;
        uint32_t y = (uint32_t) *src++;
        eax <<= 13;
        eax += (y - 0x24) * 91 + (x - 0x24);
        do {
            *p++ = (uint8_t) eax;
            eax >>= 8;
        } while (eax & (1 << 12));
    }
}

#pragma pack(push, 1)
typedef struct {
    uint64_t    env_id;
    uint64_t    env_flags;
    uint64_t    win_kernel32;       // handle of kernel32.dll
    uint64_t    win_GetProcAddress; // pointer to kernel32!GetProcAddress
    void       *ptr_alloc_rwx;      // pointer to function
    void       *ptr_alloc;          // pointer to function
    void       *ptr_alloc_zeroed;   // pointer to function
    void       *ptr_dealloc;        // pointer to function
    void       *ptr_realloc;        // pointer to function
    void       *ptr_read_stdio;     // pointer to function
    void       *ptr_write_stdio;    // pointer to function
} PLATFORM_DATA;
#pragma pack(pop)

#define ENV_ID_UNKNOWN              0
#define ENV_ID_WINDOWS              1
#define ENV_ID_LINUX                2
#define ENV_ID_WASM                 3
#define ENV_ID_MACOS                4
#define ENV_FLAGS_LINUX_STYLE_CHKSTK    0x0001  // disables __chkstk in binaries compiled with Windows target
#define ENV_FLAGS_NATIVE                0x0002  // indicates the binary is running without the loader
#define ENV_FLAGS_NO_EXIT               0x0004  // do not call SYS_exitgroup on Linux (support fn-impl scenarios)

#if !defined(_WIN32) && !defined(__linux__)
BASMCALL void *svc_alloc(size_t size, size_t align) {
    return malloc(size);
}
BASMCALL void *svc_alloc_zeroed(size_t size, size_t align) {
    return calloc(1, size);
}
BASMCALL void svc_free(void *ptr, size_t size, size_t align) {
    free(ptr);
}
BASMCALL void *svc_realloc(void* memblock, size_t old_size, size_t old_align, size_t new_size) {
    // This won't be called in loader stub.
    // Also, the main executable will directly call OS APIs/syscalls
    return realloc(memblock, new_size);
}
BASMCALL size_t svc_read_stdio(size_t fd, void *buf, size_t count) {
    if (fd != 0) return 0;
    return fread(buf, 1, count, stdin);
}
BASMCALL size_t svc_write_stdio(size_t fd, void *buf, size_t count) {
    if (fd != 1 && fd != 2) return 0;
    return fwrite(buf, 1, count, (fd == 1) ? stdout : stderr);
}
#endif

BASMCALL void *svc_alloc_rwx(size_t size) {
#ifdef _WIN32
    size_t ret = (size_t) VirtualAlloc(NULL, size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
#else
    size_t ret = (size_t) syscall(9, NULL, size, 0x7, 0x22, -1, 0);
    if (ret == (size_t)-1) ret = 0;
#endif
    return (void *) ret;
}

typedef int (BASMCALL *stub_ptr)(void *, void *);

#define STUB_RAW "\x57\x56\x53\x41\x54\x41\x55\x41\x56\x41\x57\xc8\x28\x00\x00\x52\x5e\x51\x5b\x31\xc0\xac\x49\x89\xc5\xac\x49\x89\xc6\xac\x49\x89\xc7\xac\x89\xc1\xb0\x03\xd3\xe0\x05\x00\x08\x00\x00\x49\x94\xad\x91\xff\x53\x20\x50\x49\x91\xad\x49\x89\xf0\x96\x53\x55\x48\x8d\x7c\x24\xfe\x4c\x29\xe4\x4c\x29\xe4\x44\x89\xe1\x66\xb8\x00\x04\xfd\xf3\x66\xab\xfc\x54\x5d\x83\xc8\xff\x48\x83\xc0\x02\x50\x50\x56\x6a\xff\x51\x93\xe8\x49\x00\x00\x00\x52\xe8\x2e\x00\x00\x00\x0f\xb7\x44\x75\x00\x8b\x55\xe4\xc1\xea\x0b\x0f\xaf\xd0\x29\x55\xe4\x29\x55\xe8\x73\x0c\x89\x55\xe4\x01\x55\xe8\x99\x2d\xe1\x07\x00\x00\xc1\xe8\x05\x66\x29\x44\x75\x00\xf7\xda\x5a\xc3\x80\x7d\xe7\x00\x75\x0e\x48\xc1\x65\xe4\x08\x41\x8a\x00\x49\xff\xc0\x88\x45\xe8\xc3\x5f\x4c\x89\xc9\x44\x88\xf0\x88\xc7\x5e\x56\x20\xcf\x44\x21\xe9\xc1\xe6\x05\x8d\x74\x4e\x40\xff\xd7\x99\x58\x72\x46\x44\x89\xf9\xd3\xe3\xb3\x00\x8d\x8c\x5b\x00\x08\x00\x00\x8d\x5a\x01\x04\xfd\x18\xd2\x20\xd0\x3c\x07\x73\xf6\x50\x3c\x04\x72\x10\xb7\x01\x8b\x45\xfc\x48\xf7\xd8\x41\x32\x14\x01\x30\xde\x20\xf7\xd1\xe2\x89\xde\x21\xd6\x01\xde\x01\xce\xff\xd7\x10\xdb\x73\xec\x99\xe9\x03\x01\x00\x00\x89\xf3\x8d\x74\x82\x10\x04\xf9\x18\xc0\x24\x03\x50\xff\xd7\x72\x0c\x0f\x10\x45\xf0\x0f\x11\x45\xec\xb2\x5b\xeb\x32\xff\xc6\xff\xd7\x72\x10\x8d\x73\x01\xff\xd7\x72\x1f\x83\x4d\xd8\x09\xe9\xc5\x00\x00\x00\xb2\x03\x8b\x5d\xfc\xff\xc6\xff\xca\x87\x5c\x95\xf0\x74\x04\xff\xd7\x72\xf2\x89\x5d\xfc\x83\x4d\xd8\x08\xb2\x94\x8d\x34\xd2\x99\xff\xd7\xff\xc6\x8d\x1c\xce\xb1\x03\x73\x11\xb2\x01\xff\xd7\x73\x08\x8d\x5e\x7f\xb1\x08\x83\xc2\xe2\x83\xeb\x80\x6a\x01\x5e\x56\x56\x01\xde\xff\xd7\x5e\x11\xf6\xe2\xf6\x8d\x5c\xd6\xf9\x83\x7d\xd8\x04\x5a\x53\x73\x6e\x83\x45\xd8\x07\x83\xeb\x04\x19\xc0\x21\xc3\x8d\x5c\xda\x4f\x52\x8d\x34\xda\xff\xd7\x11\xd2\x89\xd1\x83\xe9\x40\x72\xf2\x5b\x83\xf9\x04\x72\x43\x89\xde\xd1\xe9\xd3\xd3\xff\xc9\xf6\xd2\xb6\x02\x01\xda\x83\xf9\x06\x72\x1e\xff\xc9\xe8\xc1\xfe\xff\xff\xd1\x6d\xe4\x8b\x55\xe4\x39\x55\xe8\x72\x06\x29\x55\xe8\x0f\xab\xcb\x83\xf9\x04\x75\xe3\x99\x56\x01\xd6\xff\xd7\x5e\x11\xf6\xe2\xf6\x11\xc9\xd1\xee\x75\xfa\x01\xd9\xff\xc1\x89\x4d\xfc\x74\x1b\x5a\x8b\x4d\xfc\x48\xf7\xd9\x41\x0f\xb6\x1c\x09\x41\x88\x19\x49\xff\xc1\xff\xca\x79\xeb\xe9\x8c\xfe\xff\xff\x4a\x8d\x64\x64\x30\x5d\x59\x58\x49\x03\x41\xf8\xff\xd0\xc9\x41\x5f\x41\x5e\x41\x5d\x41\x5c\x5b\x5e\x5f\xc3\x00"
#if defined(__GNUC__)
__attribute__ ((section (".text#"))) const char stub_raw[] = STUB_RAW;
stub_ptr get_stub() {
    return (stub_ptr) stub_raw;
}
#else
const char stub_raw[] = STUB_RAW;
stub_ptr get_stub() {
    char *stub = (char *) svc_alloc_rwx(4096);
    for (size_t i = 0; i < sizeof(stub_raw); i++) stub[i] = stub_raw[i];
    return (stub_ptr) stub;
}
#endif
char payload[][1820] = {
"%Q$$,$JJ$$0\\GM%Q-$Zx[k+4WY1vYSet\\|mFmO^+}5q^b\?H;]hiLz6M.3S0}p88'Zp(7&]sR;{s'rS'qefR_\?j_<~M43wr}Bi2Nui|qKBhRw1xGax2Z__q}n402%*yH5.=7(iLytCn0Vb:nkEo%WNHpp5VmuU)6{]aW)&ByHd&5sgKX)<YwsmkJi+wa\\RJaW\\>X.T&=cH,Cv*du:/yj7:f$H[KCG'1SSXXkSBcc9Cq'c;3,tdB3LV'bq*-GkiSK7T)+.,H9^t\\>EJpVa<zD]b^w@(IQcEg=L5wxMbS[%GWZe{Sr{Vs|l}`}*UuJyto`3'*MDfE}\\w:KsP)h)Z\?:kE*ifM&sR;cEgx@@^~z\\|8g,1rO]T~ZC90]T,i:+@4;b]^`dCT'&U*>Ppm^OMkwp.`nZ91b:;Bc;u@r9s`-4b>cIOPgznppSn+4sAN&&5w(p<J,~cn'd&E5K`2mxQAl~3,NHpxx8m~G$OfyK[ns{)JIfn*vRk9`)J\\0w)OJox2%@Y\?8}**e;aLpjM+uw{1K}GLE1Xz@}GL%p4_vsuTz/2L3zKH;8HbtuYQ)qG\\b3nb)iis`U7[@aA\\}Wx;Vxfn|x=J.~,>Bf&|8zgHv=\?17+]:DogWn;s3Qy&e&0.M{>I;dMh6<z>14~;E20Ts+a`{QOaqVP+>IVDu{|L=RWkErcCNRR]Xhqqk\?fwLBvd5||l2YJ:wse73.G$]'Jc20{02+(]84LEI1t}]A1B2{c{s5Cp3BV99K@+1FyHYKeA%S,vz^}^%N6@\\K};ECimy2bdduh^'2'GY\\:yKq0:D-v|WIUUFJKR)-e.4^SIjC-c*T4vN4lN]z%*=A7pFRL2\?HCXzMp&V0.9[HYYom7wd5zwEw4kn{x9(%+Pg{.x<kL3[*WV-wl&6':@5vRVS.P7oXCt%>=jwFvAM1j($)kguH3iOfuREC'ovhKvbXbs/F9q/w$`BOAY0lzVSK9wcyI^+lWB\\rTpOb\\_bJTpn+mxkCg&0NwbWhnmWL}r-bvQ}E@ehDONq./^,Ny['U$whzY]3$]vcBGoSsvU-063i2/E2[.5<(5hl/ndiGBZR``Bb3+NuC](RN{xp&Or1Kce_W55X_'uDZK/Kkdn`8o}GmQ;MPgvj8A;;R:PN*/^~'jy5x1m_-evMNI\\d1E%:o's'e@0\?3$QddWd6b:^T,00MP-}GT8B@P,R/mS>2y7AtN`yMn*b^11.-HDA6VwOhy\?2jlv5X&*K/v^}uWdH@u431s[Yk:{I/8s>)52BM3t\\wm~$$d+1R2iTN5mBJ\?8zR6WUClMpr]4^rtJyY5@*'R+vSmlUF%/{C54\?_B/D;63S(y$GGN_%EkKDVH%IH`Gv{2P@BB`L\?BkpMTP%ce=u5'o%Zyj<rv:/'dnHt,V])z4Dh75(~F]k9\\[wF\\18g&spsN+CwopS:{4)t0y{^A`g{>+RJmnC{\\SEevtr89KZxM|Bms~>'r:h'S->4I@yI0r+KS^)lp-$(pIREt}eyy(|zk/\?k)5JFSdj8f.U~9Fk<bRyo*-%z3C.zr/./^z6-\\n\\Ge\\z)}i['KUD77Di~}\\S;:&/F1@&M)xr*@eQeWb=VH:<1{yNO3doy1gqi\\1'\?C42MZiZ(2=$-mCY3jS[gloYIh*X=Zh&*jMIH8;Trc<RW<1=Kb$H{@m$^'x94}r9ei%z~\\X@TOPlmwjA]9D)fJOi&nxfbycW=rD6uPFF=p1+/ZaJ1f/9vevCp[1)b><pv;9yj[Hz1$0'e>fqkywf5MOaJvo|Q*+u_vDX$\?/{z1|;pd;jKUYq:k1Mrw,9=JkCbZCPAd&Afy(xdI2z$&6(Qg[7\\5!",
};

#if defined(__linux__) && (defined(BOJ) || defined(BASM_CI))
int main() {}
#ifdef __cplusplus
extern "C"
#endif
int __libc_start_main(
    void *func_ptr,
    int argc,
    char* argv[],
    void (*init_func)(void),
    void (*fini_func)(void),
    void (*rtld_fini_func)(void),
    void *stack_end) {
#else
int main(int argc, char *argv[]) {
#endif
    PLATFORM_DATA pd;
    if (sizeof(size_t) != 8) {
        // Cannot run amd64 binaries on non-64bit environment
        return 1;
    }
    pd.env_flags            = 0; // necessary since pd is on stack
#if defined(_WIN32)
    pd.env_id               = ENV_ID_WINDOWS;
#elif defined(__linux__)
    pd.env_id               = ENV_ID_LINUX;
    // Linux's stack growth works differently than Windows.
    // Hence, we disable the __chkstk mechanism on Linux.
    pd.env_flags            |= ENV_FLAGS_LINUX_STYLE_CHKSTK;
#else
    pd.env_id               = ENV_ID_UNKNOWN;
#endif
#if defined(_WIN32)
    pd.win_kernel32         = (uint64_t) GetModuleHandleW(L"kernel32");
    pd.win_GetProcAddress   = (uint64_t) GetProcAddress;
#endif
    pd.ptr_alloc_rwx        = (void *) svc_alloc_rwx;
#if !defined(_WIN32) && !defined(__linux__)
    pd.ptr_alloc            = (void *) svc_alloc;
    pd.ptr_alloc_zeroed     = (void *) svc_alloc_zeroed;
    pd.ptr_dealloc          = (void *) svc_free;
    pd.ptr_realloc          = (void *) svc_realloc;
    pd.ptr_read_stdio       = (void *) svc_read_stdio;
    pd.ptr_write_stdio      = (void *) svc_write_stdio;
#endif

    stub_ptr stub = get_stub();
#if defined(__linux__)
    uint8_t stubbuf[68 + 580] = "H;|DR:$$$|7x6E69i$6',&%Q$$?@GjeBmVodz$C?$$c7h{.>j<g9%Q$$Q80&F$$$f5U$5L@=aT8S92:|1&.C!";
    b91tobin(stubbuf, (char const *)stubbuf);
    /* prepend thunk and relocate stub onto stack */
    for (size_t i = 0; i < 580; i++) stubbuf[68 + i] = (uint8_t)stub_raw[i];
    size_t base = ((size_t)stub_raw) & 0xFFFFFFFFFFFFF000ULL; // page-aligned pointer to munmap in thunk
    size_t len = (((size_t)stub_raw) + sizeof(stub_raw)) - base;
    len = ((len + 0xFFF) >> 12) << 12;
    *(uint64_t *)(stubbuf + 0x08) = (uint64_t) base;
    *(uint32_t *)(stubbuf + 0x11) = (uint32_t) len;
    base = ((size_t)stubbuf) & 0xFFFFFFFFFFFFF000ULL;
    len = (((size_t)stubbuf) + 68 + 580) - base;
    len = ((len + 0xFFF) >> 12) << 12;
    syscall(10, base, len, 0x7); // mprotect: make the stub on stack executable
    pd.ptr_alloc_rwx = (void *) (stubbuf + 0x1c); // thunk implements its own svc_alloc_rwx
    stub = (stub_ptr) stubbuf;
#endif
    b91tobin(payload, (char const *)payload);
    return stub(&pd, payload);
}
// LOADER END
