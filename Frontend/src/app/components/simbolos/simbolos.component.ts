import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Archivo } from 'src/app/models/Archivo';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-simbolos',
  templateUrl: './simbolos.component.html',
  styleUrls: ['./simbolos.component.css']
})
export class SimbolosComponent implements OnInit {
  archivo : Archivo = {
    texto: ''
  };
  
  constructor(private service: UserService, private router: Router, private activatedRoute: ActivatedRoute) { }
  ngOnInit(): void {}

  MostrarErrores(){
    this.service.getTablaSimbolos().subscribe(
      res => {
        this.archivo = res;
        console.log(res);
      },
      err => console.log(err)
    );
  }
}