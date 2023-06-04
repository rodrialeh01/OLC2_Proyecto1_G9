import { Component, HostBinding, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { graphviz } from 'd3-graphviz';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-ast',
  templateUrl: './ast.component.html',
  styleUrls: ['./ast.component.css']
})
export class AstComponent implements OnInit{
  @HostBinding('attr.class') cssClass = 'row';

  constructor(private service: UserService, private router:Router, private activatedRoute: ActivatedRoute) { }
  
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

  generateAST(){
    this.graph();
  }

  graph(){
    graphviz('#chart').renderDot('digraph { a -> b; }');
  }
}
