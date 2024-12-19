#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;
#if defined(__cplusplus)
extern "C" {
#endif

extern void _ThreshDetect_reg(void);
extern void _ampanmda_reg(void);
extern void _distrt_reg(void);
extern void _fi_reg(void);
extern void _kamt_reg(void);
extern void _kdrmt_reg(void);
extern void _naxn_reg(void);

void modl_reg() {
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");
    fprintf(stderr, " \"ThreshDetect.mod\"");
    fprintf(stderr, " \"ampanmda.mod\"");
    fprintf(stderr, " \"distrt.mod\"");
    fprintf(stderr, " \"fi.mod\"");
    fprintf(stderr, " \"kamt.mod\"");
    fprintf(stderr, " \"kdrmt.mod\"");
    fprintf(stderr, " \"naxn.mod\"");
    fprintf(stderr, "\n");
  }
  _ThreshDetect_reg();
  _ampanmda_reg();
  _distrt_reg();
  _fi_reg();
  _kamt_reg();
  _kdrmt_reg();
  _naxn_reg();
}

#if defined(__cplusplus)
}
#endif
