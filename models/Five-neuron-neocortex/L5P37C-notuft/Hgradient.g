//genesis - function

//Function for setting up Ih density gradient from Stuart & Spruston

function Hgradient(cellname,ch_name,base_dens,end_dens,d_half,steep)
  str ch_name,cellname
  float base_dens,end_dens,dens,d_half,steep
  str wild_path = {{cellname} @ "/##[]/" @ {ch_name}}
  str obj_path
  str soma_path = {{cellname} @ "/soma"}
  float x0 = {getfield {soma_path} x}
  float y0 = {getfield {soma_path} y}
  float z0 = {getfield {soma_path} z}
  float x,y,z,surf,dist

  foreach obj_path ({el {wild_path}})
     x = {getfield {obj_path} x}
     y = {getfield {obj_path} y}
     z = {getfield {obj_path} z}
     dist = {sqrt {((x-x0)**2)+((y-y0)**2)+((z-z0)**2)}}
     dens = base_dens + ((end_dens - base_dens) / (1 + {exp {((d_half - dist) / steep)}}))

//     echo {dens}
     
     surf = {getfield {obj_path} surface}
     setfield {obj_path} Gbar {dens*surf}

  end
end

     



