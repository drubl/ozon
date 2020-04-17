import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
@Output() backEmitter: EventEmitter<any> = new EventEmitter();
  constructor() { }

  ngOnInit(): void {
  }
  goToBack(){
    this.backEmitter.emit();
  }
}
