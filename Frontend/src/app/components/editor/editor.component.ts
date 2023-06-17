import { Component, HostBinding, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Archivo } from 'src/app/models/Archivo';
import { Consola } from 'src/app/models/Consola';
import { Message } from 'src/app/models/Message';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent implements OnInit {
  
  @HostBinding('class') classes = 'row';
  
  ngOnInit(): void {}
  
  archivo: Archivo = {
    texto: '',
  }

  consola: Consola = {
    texto: 'PyTypeCraft Console\nCopyright (C) PyTypeCraft-OLC2-P1.\nCreated by Rodrigo Hernández & Andrea Cabrera 2023',
  }

  response: Message = {
    message: '',
  }

  constructor(private service: UserService, private router: Router, private activadedRoute: ActivatedRoute) { }

  ejecutar(){
    console.log("CLICK AL BOTÓN");
    console.log(this.archivo.texto);
    this.service.ejecutar(this.archivo).subscribe(
      res => {
        console.log(res);
        this.response = res;
        this.obtConsola(this.response);
      },
      err => console.log(err)
    )
  }

  Compilar(){
    console.log(this.archivo.texto);
    this.service.C3D(this.archivo).subscribe(
      res => {
        console.log(res);
        this.response = res;
        this.obtConsola(this.response);
      },
      err => console.log(err)
    )
  }

  obtConsola(texto: Message){
    this.consola.texto = 'PyTypeCraft Console\nCopyright (C) PyTypeCraft-OLC2-P1.\nCreated by Rodrigo Hernández & Andrea Cabrera 2023\n\n' + texto.message ;
    console.log("CONSOLA");
  }
}