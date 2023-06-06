import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Archivo } from 'src/app/models/Archivo';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-errores',
  templateUrl: './errores.component.html',
  styleUrls: ['./errores.component.css']
})
export class ErroresComponent implements OnInit {
  archivo : Archivo = {
    texto: ''
  };
  
  constructor(private service: UserService, private router: Router, private activatedRoute: ActivatedRoute) { }
  ngOnInit(): void {}

  MostrarErrores(){
    this.service.getTablaErrores().subscribe(
      res => {
        this.archivo = res;
      },
      err => console.log(err)
    );
  }
}
