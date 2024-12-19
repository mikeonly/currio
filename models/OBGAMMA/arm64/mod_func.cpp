#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;
#if defined(__cplusplus)
extern "C" {
#endif

extern void _CaPN_reg(void);
extern void _CaT_reg(void);
extern void _Caint_reg(void);
extern void _Can_reg(void);
extern void _GradNMDA_reg(void);
extern void _GradeAMPA_reg(void);
extern void _GradeGABA_reg(void);
extern void _KCa_reg(void);
extern void _KDRmt_reg(void);
extern void _KS_reg(void);
extern void _LCa_reg(void);
extern void _NaP_reg(void);
extern void _Naxn_reg(void);
extern void _Nicotin_reg(void);
extern void _OdorInput_reg(void);
extern void _SineInput_reg(void);
extern void _cadecay_reg(void);
extern void _cadecay2_reg(void);
extern void _hpg_reg(void);
extern void _kAmt_reg(void);
extern void _kM_reg(void);
extern void _kfasttab_reg(void);
extern void _kslowtab_reg(void);
extern void _nafast_reg(void);
extern void _nmdanet_reg(void);

void modl_reg() {
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");
    fprintf(stderr, " \"CaPN.mod\"");
    fprintf(stderr, " \"CaT.mod\"");
    fprintf(stderr, " \"Caint.mod\"");
    fprintf(stderr, " \"Can.mod\"");
    fprintf(stderr, " \"GradNMDA.mod\"");
    fprintf(stderr, " \"GradeAMPA.mod\"");
    fprintf(stderr, " \"GradeGABA.mod\"");
    fprintf(stderr, " \"KCa.mod\"");
    fprintf(stderr, " \"KDRmt.mod\"");
    fprintf(stderr, " \"KS.mod\"");
    fprintf(stderr, " \"LCa.mod\"");
    fprintf(stderr, " \"NaP.mod\"");
    fprintf(stderr, " \"Naxn.mod\"");
    fprintf(stderr, " \"Nicotin.mod\"");
    fprintf(stderr, " \"OdorInput.mod\"");
    fprintf(stderr, " \"SineInput.mod\"");
    fprintf(stderr, " \"cadecay.mod\"");
    fprintf(stderr, " \"cadecay2.mod\"");
    fprintf(stderr, " \"hpg.mod\"");
    fprintf(stderr, " \"kAmt.mod\"");
    fprintf(stderr, " \"kM.mod\"");
    fprintf(stderr, " \"kfasttab.mod\"");
    fprintf(stderr, " \"kslowtab.mod\"");
    fprintf(stderr, " \"nafast.mod\"");
    fprintf(stderr, " \"nmdanet.mod\"");
    fprintf(stderr, "\n");
  }
  _CaPN_reg();
  _CaT_reg();
  _Caint_reg();
  _Can_reg();
  _GradNMDA_reg();
  _GradeAMPA_reg();
  _GradeGABA_reg();
  _KCa_reg();
  _KDRmt_reg();
  _KS_reg();
  _LCa_reg();
  _NaP_reg();
  _Naxn_reg();
  _Nicotin_reg();
  _OdorInput_reg();
  _SineInput_reg();
  _cadecay_reg();
  _cadecay2_reg();
  _hpg_reg();
  _kAmt_reg();
  _kM_reg();
  _kfasttab_reg();
  _kslowtab_reg();
  _nafast_reg();
  _nmdanet_reg();
}

#if defined(__cplusplus)
}
#endif
