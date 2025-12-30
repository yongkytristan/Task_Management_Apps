<template>
  <div class="flex h-screen bg-gray-50 dark:bg-gray-900 overflow-hidden">
    
    <!-- Sidebar -->
    <aside class="w-64 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 flex flex-col hidden md:flex">
      <div class="h-16 flex items-center px-6 border-b border-gray-100 dark:border-gray-700">
        <div class="w-8 h-8 bg-teal-600 rounded-lg flex items-center justify-center text-white font-bold shadow-md mr-3">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
        </div>
        <div>
          <h1 class="text-lg font-bold text-gray-800 dark:text-white tracking-tight">TaskManageApps</h1>
          <p class="text-[10px] text-gray-400 font-medium">Manage your tasks</p>
        </div>
      </div>

      <nav class="flex-1 px-4 py-6 space-y-1 overflow-y-auto">
        <button 
          @click="filterStatus = ''" 
          :class="`w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all ${filterStatus === '' ? 'bg-teal-50 text-teal-700 dark:bg-teal-900/20 dark:text-teal-300' : 'text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700/50'}`"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3 opacity-70" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
          </svg>
          All Tasks
          <span v-if="taskCounts.all > 0" class="ml-auto bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 py-0.5 px-2 rounded-md text-xs font-bold">{{ taskCounts.all }}</span>
        </button>

        <button 
          @click="filterStatus = 'To Do'" 
          :class="`w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all ${filterStatus === 'To Do' ? 'bg-teal-50 text-teal-700 dark:bg-teal-900/20 dark:text-teal-300' : 'text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700/50'}`"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3 opacity-70" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          To Do
          <span v-if="taskCounts.todo > 0" class="ml-auto bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 py-0.5 px-2 rounded-md text-xs font-bold">{{ taskCounts.todo }}</span>
        </button>

        <button 
          @click="filterStatus = 'In Progress'" 
          :class="`w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all ${filterStatus === 'In Progress' ? 'bg-teal-50 text-teal-700 dark:bg-teal-900/20 dark:text-teal-300' : 'text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700/50'}`"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3 opacity-70" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
          In Progress
          <span v-if="taskCounts.inprogress > 0" class="ml-auto bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 py-0.5 px-2 rounded-md text-xs font-bold">{{ taskCounts.inprogress }}</span>
        </button>

        <button 
          @click="filterStatus = 'Done'" 
          :class="`w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all ${filterStatus === 'Done' ? 'bg-teal-50 text-teal-700 dark:bg-teal-900/20 dark:text-teal-300' : 'text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700/50'}`"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3 opacity-70" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          Done
          <span v-if="taskCounts.done > 0" class="ml-auto bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 py-0.5 px-2 rounded-md text-xs font-bold">{{ taskCounts.done }}</span>
        </button>
      </nav>

      <div class="p-4 border-t border-gray-100 dark:border-gray-700">
        <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700/50 transition-colors cursor-pointer group relative">
           <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-600 shadow-sm" src="https://ui-avatars.com/api/?name=User+Nickname&background=random" alt="User" />
           <div class="flex-1 min-w-0">
             <p class="text-sm font-bold text-gray-900 dark:text-white truncate">User Nickname</p>
             <p class="text-xs text-gray-500 truncate">user@taskmanageapps.com</p>
           </div>
           
           <button @click="$emit('logout')" class="text-gray-400 hover:text-red-500 transition-colors" title="Sign Out">
             <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
             </svg>
           </button>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 overflow-y-auto">
      <div class="max-w-5xl mx-auto px-6 py-10">
        
        <!-- Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-10">
          <div>
            <h2 class="text-3xl font-bold text-gray-900 dark:text-white tracking-tight">My Tasks</h2>
            <p class="text-gray-500 dark:text-gray-400 mt-1">Organize and track your daily tasks</p>
          </div>
          <div class="flex items-center gap-3">
            <button 
              @click="toggleTheme" 
              class="p-3 bg-white dark:bg-gray-800 text-gray-500 dark:text-gray-400 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
              title="Toggle Theme"
            >
               <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
               </svg>
               <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
               </svg>
            </button>
            <button 
              @click="modalOpen = true; isEditing = false; resetForm()"
              class="flex items-center justify-center gap-2 px-6 py-3 bg-teal-600 hover:bg-teal-700 text-white font-bold rounded-xl shadow-lg shadow-teal-500/30 transition-all transform active:scale-95"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
               New Task
            </button>
          </div>
        </div>

        <!-- Inline Tabs for Mobile -->
        <div class="flex space-x-1 p-1 bg-gray-100/50 dark:bg-gray-800/50 rounded-xl w-fit mb-8 md:hidden">
          <button 
            v-for="status in ['', 'To Do', 'In Progress', 'Done']" 
            :key="status"
            @click="filterStatus = status"
            :class="`px-4 py-2 text-sm font-bold rounded-lg transition-all ${filterStatus === status ? 'bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-sm' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'}`"
          >
            {{ status || 'All Tasks' }}
          </button>
        </div>
        
        <!-- Filter Tabs for Desktop -->
        <div class="hidden md:flex space-x-2 mb-8 border-b border-gray-100 dark:border-gray-700 pb-1">
           <button 
            v-for="tab in [{label: 'All Tasks', val: ''}, {label: 'To Do', val: 'To Do'}, {label: 'In Progress', val: 'In Progress'}, {label: 'Done', val: 'Done'}]" 
            :key="tab.val"
            @click="filterStatus = tab.val"
            :class="`px-4 py-2 text-sm font-bold rounded-lg transition-all relative ${filterStatus === tab.val ? 'text-teal-600 bg-teal-50 dark:bg-teal-900/20' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50 dark:hover:text-gray-300 dark:hover:bg-gray-800'}`"
          >
            {{ tab.label }}
          </button>
        </div>

        <!-- Task List -->
        <div class="space-y-4">
          <div v-if="filteredTasks.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-2xl border border-dashed border-gray-200 dark:border-gray-700">
             <div class="inline-flex w-16 h-16 bg-gray-50 dark:bg-gray-700 rounded-full items-center justify-center mb-4">
               <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
               </svg>
             </div>
             <p class="text-gray-500 dark:text-gray-400 font-medium">No tasks found</p>
          </div>

          <div 
            v-for="task in filteredTasks" 
            :key="task.id" 
            class="bg-white dark:bg-gray-800 rounded-2xl p-6 border border-gray-100 dark:border-gray-700 shadow-sm hover:shadow-md transition-all flex flex-col sm:flex-row gap-4 sm:items-start group"
          >
            <!-- Checkbox Custom -->
            <div class="pt-1">
              <div class="w-6 h-6 rounded-full border-2 flex items-center justify-center cursor-pointer transition-colors"
                :class="task.status === 'Done' ? 'bg-emerald-500 border-emerald-500' : 'border-gray-300 dark:border-gray-600 hover:border-teal-500'"
                @click="toggleStatus(task)"
              >
                 <svg v-if="task.status === 'Done'" xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                 </svg>
              </div>
            </div>

            <div class="flex-1 min-w-0">
               <div class="flex items-center gap-3 mb-1">
                 <h3 :class="`text-lg font-bold text-gray-900 dark:text-white truncate ${task.status === 'Done' ? 'line-through text-gray-400' : ''}`">{{ task.title }}</h3>
                 <span :class="`px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusColor(task.status)}`">
                    {{ task.status }}
                 </span>
               </div>
               <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed mb-3">{{ task.description || 'No description provided.' }}</p>
               
               <!-- Date Display -->
               <div v-if="task.start_date || task.end_date" class="flex flex-wrap items-center gap-3 text-xs text-gray-400 font-medium mt-2">
                 <div v-if="task.start_date" class="flex items-center gap-1 bg-gray-50 dark:bg-gray-700/50 px-2 py-1 rounded-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                    <span>Start: {{ formatDate(task.start_date) }}</span>
                 </div>
                 <div v-if="task.end_date" class="flex items-center gap-1 bg-gray-50 dark:bg-gray-700/50 px-2 py-1 rounded-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <span>End: {{ formatDate(task.end_date) }}</span>
                 </div>
               </div>
            </div>

            <div class="flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
              <button @click="startEdit(task)" class="p-2 text-gray-400 hover:text-teal-600 hover:bg-teal-50 dark:hover:bg-teal-900/20 rounded-lg transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              </button>
              <button @click="deleteTask(task.id)" class="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Modal Form -->
    <div v-if="modalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm transition-all" @click.self="modalOpen = false">
      <div class="bg-white dark:bg-gray-800 w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden transform transition-all h-auto max-h-[90vh] overflow-y-auto">
        <div class="px-6 py-4 border-b border-gray-100 dark:border-gray-700 flex justify-between items-center bg-gray-50 dark:bg-gray-900/50">
           <h3 class="text-lg font-bold text-gray-900 dark:text-white">{{ isEditing ? 'Edit Task' : 'Create New Task' }}</h3>
           <button @click="modalOpen = false" class="text-gray-400 hover:text-gray-500">
             <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
             </svg>
           </button>
        </div>
        
        <form @submit.prevent="handleSubmit" class="p-6 space-y-4">
          <div>
            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wide mb-1.5">Title</label>
            <input v-model="form.title" required class="w-full px-4 py-3 bg-gray-50 dark:bg-gray-700 border-none rounded-xl focus:ring-2 focus:ring-teal-500 outline-none font-medium text-gray-900 dark:text-white" placeholder="e.g. Design Landing Page" />
          </div>
          
          <div>
            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wide mb-1.5">Description</label>
            <textarea v-model="form.description" rows="3" class="w-full px-4 py-3 bg-gray-50 dark:bg-gray-700 border-none rounded-xl focus:ring-2 focus:ring-teal-500 outline-none text-gray-900 dark:text-white" placeholder="Add details..."></textarea>
          </div>
          
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-gray-500 uppercase tracking-wide mb-1.5">Start Date & Time</label>
               <input v-model="form.start_date" type="datetime-local" class="w-full px-4 py-3 bg-gray-50 dark:bg-gray-700 border-none rounded-xl focus:ring-2 focus:ring-teal-500 outline-none text-gray-900 dark:text-white text-sm" />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-500 uppercase tracking-wide mb-1.5">End Date & Time</label>
               <input v-model="form.end_date" type="datetime-local" class="w-full px-4 py-3 bg-gray-50 dark:bg-gray-700 border-none rounded-xl focus:ring-2 focus:ring-teal-500 outline-none text-gray-900 dark:text-white text-sm" />
            </div>
          </div>

          <div>
            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wide mb-1.5">Status</label>
            <div class="flex gap-2">
               <button type="button" v-for="s in ['To Do', 'In Progress', 'Done']" :key="s"
                 @click="form.status = s"
                 :class="`flex-1 py-2.5 rounded-xl text-sm font-bold border-2 transition-all ${form.status === s ? getStatusBorder(s) + ' bg-gray-50 dark:bg-gray-700' : 'border-gray-100 dark:border-gray-700 text-gray-400 hover:border-gray-200'}`"
               >
                 {{ s }}
               </button>
            </div>
          </div>

          <div class="pt-4 flex gap-3">
            <button type="button" @click="modalOpen = false" class="flex-1 py-3 text-gray-700 dark:text-gray-200 font-bold hover:bg-gray-50 dark:hover:bg-gray-700 rounded-xl transition-colors">Cancel</button>
            <button type="submit" :disabled="isSubmitting" class="flex-1 py-3 bg-teal-600 text-white font-bold rounded-xl hover:bg-teal-700 shadow-lg shadow-teal-500/30 transition-all disabled:opacity-50 disabled:cursor-not-allowed">
              {{ isSubmitting ? 'Saving...' : (isEditing ? 'Save Changes' : 'Create Task') }}
            </button>
          </div>
          
          <div v-if="submitError" class="text-sm text-red-600 text-center bg-red-50 dark:bg-red-900/20 p-2 rounded-lg">
            {{ submitError }}
          </div>
        </form>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

defineEmits(['logout']);

// State
const tasks = ref([]);
const filterStatus = ref('');
const modalOpen = ref(false);
const isEditing = ref(false);
const isSubmitting = ref(false);
const submitError = ref('');
const form = ref({ id: null, title: '', description: '', status: 'To Do', start_date: '', end_date: '' });
const isDark = ref(false);

// Computed
const filteredTasks = computed(() => {
  let result = tasks.value;
  if (filterStatus.value) {
    result = result.filter(task => task.status === filterStatus.value);
  }
  
  // Sorting: In Progress (1) -> To Do (2) -> Done (3)
  const statusPriority = { 'In Progress': 1, 'To Do': 2, 'Done': 3 };
  
  return result.sort((a, b) => {
    const priorityA = statusPriority[a.status] || 99;
    const priorityB = statusPriority[b.status] || 99;
    
    // If status is same, sort by ID descending (newest first)
    if (priorityA === priorityB) {
      return b.id - a.id;
    }
    
    return priorityA - priorityB;
  });
});

const taskCounts = computed(() => {
  return {
    all: tasks.value.length,
    todo: tasks.value.filter(t => t.status === 'To Do').length,
    inprogress: tasks.value.filter(t => t.status === 'In Progress').length,
    done: tasks.value.filter(t => t.status === 'Done').length
  };
});

// Helpers
const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('en-US', {
    month: 'short', day: 'numeric', year: 'numeric',
    hour: 'numeric', minute: 'numeric', hour12: true
  }).format(date);
};

const getStatusColor = (status) => {
  switch (status) {
    case 'Done': return 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-300'; 
    case 'In Progress': return 'bg-teal-100 text-teal-700 dark:bg-teal-900/30 dark:text-teal-300';
    default: return 'bg-gray-100 text-gray-600 dark:bg-gray-700 dark:text-gray-300';
  }
};

const getStatusBorder = (status) => {
   switch (status) {
    case 'Done': return 'border-emerald-500 text-emerald-600'; 
    case 'In Progress': return 'border-teal-500 text-teal-600';
    default: return 'border-gray-400 text-gray-500';
  }
}

// API
const getAuthHeader = () => {
  return { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } };
};

const fetchTasks = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:5000/api/tasks', getAuthHeader());
    tasks.value = res.data;
  } catch (error) { console.error(error); }
};

const handleSubmit = async () => {
  submitError.value = '';
  isSubmitting.value = true;
  try {
    if (isEditing.value) {
      await updateTaskApi(form.value);
    } else {
      await addTaskApi(form.value);
    }
    modalOpen.value = false;
  } catch (err) {
    console.error('Submit error:', err);
    submitError.value = 'Failed to save task. ' + (err.response?.data?.msg || err.message);
  } finally {
    isSubmitting.value = false;
  }
};

const addTaskApi = async (taskData) => {
  await axios.post('http://127.0.0.1:5000/api/tasks', taskData, getAuthHeader());
  fetchTasks();
};

const updateTaskApi = async (taskData) => {
  await axios.put(`http://127.0.0.1:5000/api/tasks/${taskData.id}`, taskData, getAuthHeader());
  fetchTasks();
};

const deleteTask = async (id) => {
  if(confirm('Delete this task?')) {
    await axios.delete(`http://127.0.0.1:5000/api/tasks/${id}`, getAuthHeader());
    fetchTasks();
  }
};

const toggleStatus = async (task) => {
  const newStatus = task.status === 'Done' ? 'To Do' : 'Done';
  await updateTaskApi({ ...task, status: newStatus });
};

const startEdit = (task) => {
  // Format dates for datetime-local input (YYYY-MM-DDThh:mm)
  const formatForInput = (isoStr) => {
    if(!isoStr) return '';
    const date = new Date(isoStr);
    // Adjust to local time string but keep format
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    return `${year}-${month}-${day}T${hours}:${minutes}`;
  };

  form.value = { 
    ...task, 
    start_date: formatForInput(task.start_date),
    end_date: formatForInput(task.end_date)
  };
  isEditing.value = true;
  modalOpen.value = true;
};

const resetForm = () => {
  form.value = { id: null, title: '', description: '', status: 'To Do', start_date: '', end_date: '' };
  submitError.value = '';
};

const toggleTheme = () => {
  isDark.value = !isDark.value;
  if(isDark.value) {
    document.documentElement.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  }
};

const initTheme = () => {
  if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDark.value = true;
    document.documentElement.classList.add('dark');
  } else {
    isDark.value = false;
    document.documentElement.classList.remove('dark');
  }
};

onMounted(() => {
  fetchTasks();
  initTheme();
});
</script>