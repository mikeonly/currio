//genesis

// Added diffamp to represent spontaneous activity.

// The firing rate modulation is achieved by a separate randomspike element
// whose spike output is low-pass filtered by an RC element. The average output of the
// RC element is 1, so that the average output of the target diffamp elements remains
// unchanged, only their temporal profile is modulated (see papers by Harsch and Robinson).

// The rate of the randomspike element and the decay time constant of the RC element
// can be set. A small time-constant leads to more synchronous activation of the 
// target synapses.
 
// The output is fed as PLUS msg into a separate diffamp element that in turn will 
// set the gain of the diffamps (see Firing_rate_profile.g) driving the randomspike 
// elements (Excitatory_fibres.g).

echo blabla1

// echo gives parse error when - is used instead of _

function Harsch_Robinson_modulation (mean_rate, time_constant)
//function Harsch-Robinson_modulation (mean_rate, time_constant)

   echo blabla3

   float mean_rate, time_constant

// So to have unity average, the gain R of the RC element should be
// set to the inverse of (mean_rate) * (time_constant).
// However, the initial value caused by the pulse will be about
// dt * (R/tau} (assume we are on linear part of exponential), so we
// should also divide by this, giving a net division by dt and frequency.
// This works, but takes a long time to reach 'steady-state'.
 
    echo {mean_rate} {time_constant}


	create randomspike /HR_modulation
	setfield ^ rate {mean_rate}


	create RC /HR_modulation/RC

// change 26Feb09 want to manipulate amplitude independently, normalized at 30

//    if ({{{mean_rate} != 0} && {{time_constant} != 0}})
//         setfield ^ R {1 / {{mean_rate} * {dt}}} 
         setfield ^ R {1 / {30 * {dt}}} // {1 / {{mean_rate} * {dt}}}  // 25e-6}} 
         setfield ^ C {{time_constant} / {getfield ^ R}}
//    else setfield ^ R 0  
//         setfield ^ C 0
//    end

	addmsg /HR_modulation /HR_modulation/RC INJECT state


    create diffamp /HR_modulation/RC/diffamp
    setfield ^ plus 0.5 gain 1 saturation 10e10 // spontaneous activity
    
    addmsg /HR_modulation/RC /HR_modulation/RC/diffamp PLUS state
    
    addmsg /HR_modulation/RC/diffamp      /output/{asc_name} SAVE output
 
end




