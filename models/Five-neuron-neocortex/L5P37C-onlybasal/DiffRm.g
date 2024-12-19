//genesis - function

//Function setting differential Rm for compartments based on distance from soma

function DiffRm(cellname, Rm_base, Rm_end, d_half, steep)
  float Rm_base, Rm_end, Rm_new, d_half, steep
  str cellname
  str wild_path = {{cellname} @ "/##[][TYPE=compartment]"}
  str comp_path
  str soma_path = {{cellname} @ "/soma"}
  float x0 = {getfield {soma_path} x}
  float y0 = {getfield {soma_path} y}
  float z0 = {getfield {soma_path} z}
  float x,y,z,len,dia,surf,dist

  foreach comp_path ({el {wild_path}})
     x = {getfield {comp_path} x}
     y = {getfield {comp_path} y}
     z = {getfield {comp_path} z}
     dist = {sqrt {((x-x0)**2)+((y-y0)**2)+((z-z0)**2)}}
     Rm_new = Rm_end + ((Rm_base - Rm_end) / (1 + {exp {((d_half - dist) / - steep)}}))
     len = {getfield {comp_path} len}
     dia = {getfield {comp_path} dia}
     surf = 3.14159*dia*len
     
     if (comp_path != soma_path)
        setfield {comp_path} Rm {Rm_new/surf}
     end

  end
end


     



