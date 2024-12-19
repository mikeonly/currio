#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;
#if defined(__cplusplus)
extern "C" {
#endif

extern void _kamt_reg(void);
extern void _kdrmt_reg(void);
extern void _naxn_reg(void);
extern void _nmdanetOB_reg(void);

void modl_reg() {
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");
    fprintf(stderr, " \"kamt.mod\"");
    fprintf(stderr, " \"kdrmt.mod\"");
    fprintf(stderr, " \"naxn.mod\"");
    fprintf(stderr, " \"nmdanetOB.mod\"");
    fprintf(stderr, "\n");
  }
  _kamt_reg();
  _kdrmt_reg();
  _naxn_reg();
  _nmdanetOB_reg();
}

#if defined(__cplusplus)
}
#endif
