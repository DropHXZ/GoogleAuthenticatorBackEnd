import { Injectable } from '@angular/core';


@Injectable()
export class SystemService {
    getHostIP() { return "127.0.0.1:8000";  }
}